from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sentence_transformers import SentenceTransformer, util
from pathlib import Path
import json

# Load embedding model and metadata once at startup
model = SentenceTransformer('all-MiniLM-L6-v2')

# Set up paths
script_dir = Path(__file__).parent
metadata_path = script_dir / "images" / "floor_plan_metadata.json"

# Load metadata
with open(metadata_path, 'r') as f:
    floorplans = json.load(f)

# Build descriptions
def build_description(plan):
    description = f"A {plan['floors']}-floor house with total area of {plan['total_area']} sqft and plot size {plan['plot_size']}. "
    for floor in plan.get("floor_details", []):
        desc = f"On the {floor['floor']}, "
        if floor.get('bedrooms'):
            desc += f"{len(floor['bedrooms'])} bedroom(s), "
        if floor.get('other_rooms'):
            rooms = ', '.join([room['name'] for room in floor['other_rooms']])
            desc += f"other rooms include: {rooms}."
        description += desc + " "
    return description.strip()

descriptions = [build_description(plan) for plan in floorplans]
embeddings = model.encode(descriptions, convert_to_tensor=True)

# Deterministic image selection
def get_next_best_image(user_query, shown_images, target_floors, top_k=5):
    filtered_indices = [i for i, plan in enumerate(floorplans) if plan['floors'] == target_floors]
    if not filtered_indices:
        return None, None

    filtered_descriptions = [descriptions[i] for i in filtered_indices]
    filtered_embeddings = embeddings[filtered_indices]
    user_embedding = model.encode(user_query, convert_to_tensor=True)

    similarities = util.cos_sim(user_embedding, filtered_embeddings)[0]
    similarity_scores = similarities.cpu().tolist()

    # Stable sort by similarity score, then image name (for tie-breaking)
    ranked_local_indices = sorted(
        range(len(similarity_scores)),
        key=lambda idx: (-similarity_scores[idx], floorplans[filtered_indices[idx]]["image"])
    )

    for local_idx in ranked_local_indices:
        global_index = filtered_indices[local_idx]
        image_name = floorplans[global_index]["image"]
        if image_name not in shown_images:
            return floorplans[global_index], descriptions[global_index]

    return None, None

# Endpoint to check files in images directory
def test_images_directory(request):
    images_dir = script_dir / "images"
    result = {
        "script_dir": str(script_dir),
        "images_dir": str(images_dir),
        "images_dir_exists": images_dir.exists(),
        "files": []
    }
    if images_dir.exists():
        result["files"] = [f.name for f in images_dir.iterdir() if f.is_file()]
    return JsonResponse(result)

# Serve floor plan image
def serve_floor_plan_image(request, image_name):
    try:
        image_path = script_dir / "images" / image_name
        print(image_path)
        if not image_path.exists():
            images_dir = script_dir / "images"
            
            return JsonResponse({
                "error": f"Image not found: {image_name}",
                "searched_path": str(image_path),
                "images_dir_exists": images_dir.exists(),
                "available_files": [f.name for f in images_dir.iterdir()] if images_dir.exists() else []
            }, status=404)

        content_type = 'image/jpeg'
        if image_name.lower().endswith('.png'):
            content_type = 'image/png'
        elif image_name.lower().endswith('.gif'):
            content_type = 'image/gif'
        elif image_name.lower().endswith('.webp'):
            content_type = 'image/webp'

        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type=content_type)

    except Exception as e:
        return JsonResponse({"error": f"Error serving image: {str(e)}"}, status=500)

# Main API to generate floor plan
@csrf_exempt
def generate_floor_plan(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            length = int(data["plot_length"])
            width = int(data["plot_width"])
            floors = int(data["no_of_floors"])
            bedrooms = int(data["no_of_bedrooms"])
            bedroom_dimensions = data.get("bedroom_dimensions", [])
            shown = data.get("shown_images", [])

            # 1. Find all plans with matching floors and plot size
            matching_plans = [
                plan for plan in floorplans
                if plan['floors'] == floors and
                   int(float(plan['plot_size'].split('*')[0])) == length and
                   int(float(plan['plot_size'].split('*')[1])) == width
            ]

            # 2. If found, check for bedroom count and dimensions
            for plan in matching_plans:
                plan_bedrooms = []
                for floor in plan.get('floor_details', []):
                    plan_bedrooms.extend(floor.get('bedrooms', []))
                if len(plan_bedrooms) == bedrooms:
                    # Compare each bedroom's length and width
                    match = True
                    for i, user_bed in enumerate(bedroom_dimensions):
                        if i >= len(plan_bedrooms):
                            match = False
                            break
                        plan_bed = plan_bedrooms[i]
                        if (
                            int(plan_bed.get('length', 0)) != int(user_bed.get('length', 0)) or
                            int(plan_bed.get('width', 0)) != int(user_bed.get('width', 0))
                        ):
                            match = False
                            break
                    if match:
                        description = build_description(plan)
                        image_name = plan["image"]
                        image_url = f"/api/floor/images/{image_name}"
                        return JsonResponse({
                            "description": description,
                            "image_name": image_name,
                            "image_url": image_url,
                            "prompt": f"Exact match for {floors} floors, {length}x{width}, {bedrooms} bedrooms with specified dimensions"
                        })

            # 3. If not found, return the most suitable (closest) plan by plot size/floors
            prompt = f"Generate a {floors}-floor house plan of area {length*width} sqft ({length}*{width}) with {bedrooms} bedrooms."
            best_plan, matched_description = get_next_best_image(prompt, shown, target_floors=floors)
            if best_plan is None:
                return JsonResponse({"message": "No more matching floor plans."}, status=404)
            image_name = best_plan["image"]
            image_url = f"/api/floor/images/{image_name}"
            return JsonResponse({
                "description": matched_description,
                "image_name": image_name,
                "image_url": image_url,
                "prompt": f"No exact match for bedrooms/plot, showing closest for {floors} floors, {length}x{width}"
            })
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)
