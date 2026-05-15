from diffusers import StableDiffusionPipeline
import torch
from pathlib import Path
import os

# Use raw string (r"") or forward slashes for Windows paths
model_path ="dreambooth-floorplan\checkpoint-1"
print(f"Path exists: {os.path.exists(model_path)}")
print(f"Path contents: {os.listdir(model_path)}")
# Verify the path exists
if not Path(model_path).exists():
    raise FileNotFoundError(f"Model directory not found: {model_path}")

# Load the pipeline with safety checks disabled (optional)
pipe = StableDiffusionPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    safety_checker=None,  # Disable if you don't need NSFW filtering
    local_files_only=True  # Ensure it uses the local files
).to("cuda" if torch.cuda.is_available() else "cpu")

# Inference
prompt = "sks floorplan of a 2-bedroom house with 1 floor"
image = pipe(prompt, num_inference_steps=100).images[0]  # More steps = better quality
image.save("generated_floorplan.png")
image.show()