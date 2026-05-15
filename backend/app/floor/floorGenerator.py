import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sentence_transformers import SentenceTransformer, util
from PIL import Image
from pathlib import Path

# Load embedding model and metadata once at startup
model = SentenceTransformer('all-MiniLM-L6-v2')

# Get the directory where this script is located
script_dir = Path(__file__).parent
metadata_path = script_dir / "images" / "floor_plan_metadata.json"

with open(metadata_path, 'r') as f:
    floorplans = json.load(f)

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

def get_next_best_image(user_query, shown_images, target_floors, top_k=5):
    filtered_indices = [i for i, plan in enumerate(floorplans) if plan['floors'] == target_floors]
    if not filtered_indices:
        return None, None

    filtered_descriptions = [descriptions[i] for i in filtered_indices]
    filtered_embeddings = embeddings[filtered_indices]
    user_embedding = model.encode(user_query, convert_to_tensor=True)
    similarities = util.cos_sim(user_embedding, filtered_embeddings)[0]
    ranked_local_indices = similarities.argsort(descending=True)

    for idx in ranked_local_indices:
        global_index = filtered_indices[idx]
        image_name = floorplans[global_index]["image"]
        if image_name not in shown_images:
            return floorplans[global_index], descriptions[global_index]

    return None, None

@csrf_exempt
def generate_floor_plan(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            length = int(data["plot_length"])
            width = int(data["plot_width"])
            total_area = length * width
            floors = int(data["no_of_floors"])
            bedrooms = int(data["no_of_bedrooms"])
            prompt = f"Generate a {floors}-floor house plan of area {total_area} sqft ({length}*{width}) with {bedrooms} bedrooms."
            
            shown = data.get("shown_images", [])
            best_plan, matched_description = get_next_best_image(prompt, shown, target_floors=floors)
            
            if best_plan is None:
                return JsonResponse({"message": "No more matching floor plans."}, status=404)

            return JsonResponse({
                "description": matched_description,
                "image_name": best_plan["image"],
                "prompt": prompt
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST allowed"}, status=405)