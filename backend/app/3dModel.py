import requests
import base64
import time
import os

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Saved {filename}")

output_dir = "./output_model"
os.makedirs(output_dir, exist_ok=True)

def check_task_status(task_id, headers):
    while True:
        response = requests.get(
            f"https://api.meshy.ai/openapi/v1/image-to-3d/{task_id}",
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        status = data["status"]
        print(f"Task Status: {status}")
        if status == "SUCCEEDED":
            return data
        elif status in ["FAILED", "CANCELED"]:
            raise Exception("Task failed or was canceled.")
        time.sleep(5)  # Wait and try again

def main():
    API_KEY = "msy_Lq9wrJ2pW6VHFZKGQLLgE805az0isgbLIh1c"  # Replace with your actual API key

    image_path = "house.jpg"
    if not os.path.exists(image_path):
        print(f"Error: {image_path} does not exist.")
        return
    else:
        print(f"Image {image_path} exists.")
    image_data = open(image_path, "rb").read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    image_uri = f"data:image/jpg;base64,{image_base64}" # Public image URL or base64 string
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "image_url": image_uri,
        "ai_model": "meshy-5",
        "should_texture": True,
        "should_remesh": True
    }

    response = requests.post(
        "https://api.meshy.ai/openapi/v1/image-to-3d",
        headers=headers,
        json=payload
    )

    response.raise_for_status()
    task_id = response.json()["result"]
    print(f"Task submitted. ID: {task_id}")

    task_data = check_task_status(task_id, headers)

    model_urls = task_data["model_urls"]

    # Download the GLB model
    if "glb" in model_urls:
        download_file(model_urls["glb"], os.path.join(output_dir, "model.glb"))

    # Download textures (if any)
    for texture in task_data.get("texture_urls", []):
        for key, url in texture.items():
            download_file(url, os.path.join(output_dir, f"{key}.png"))

if __name__ == "__main__":
    main()
