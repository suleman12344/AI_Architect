import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

# HARDCODED PATHS - Edit these to match your folder structure
INPUT_FOLDER = "backend/app/2d_floor_/images"
OUTPUT_FOLDER = "backend/app/2d_floor_/deblurred_images"

def create_dir(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def sharpen_image_cv2(image_path, output_path):
    """Sharpen image using OpenCV unsharp masking technique"""
    try:
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not read image at {image_path}")
            return False
            
        # Apply Gaussian blur
        gaussian = cv2.GaussianBlur(img, (0, 0), 3.0)
        
        # Apply unsharp mask (original + (original - blurred) * factor)
        sharpened = cv2.addWeighted(img, 2.5, gaussian, -1.5, 0)
        
        # Apply additional sharpening kernel
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        sharpened = cv2.filter2D(sharpened, -1, kernel)
        
        # Save the enhanced image
        cv2.imwrite(output_path, sharpened)
        return True
    except Exception as e:
        print(f"Error in sharpen_image_cv2: {e}")
        return False

def enhance_image_pil(image_path, output_path):
    """Enhance image using PIL for sharpness, contrast, and brightness"""
    try:
        # Open image
        img = Image.open(image_path)
        
        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(2.0)
        
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.7)
        
        # Enhance brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.2)
        
        # Save enhanced image
        img.save(output_path)
        return True
    except Exception as e:
        print(f"Error in enhance_image_pil: {e}")
        return False

def denoise_image(image_path, output_path):
    """Apply denoising to image using OpenCV's fastNlMeansDenoisingColored"""
    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not read image at {image_path}")
            return False
            
        denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        cv2.imwrite(output_path, denoised)
        return True
    except Exception as e:
        print(f"Error in denoise_image: {e}")
        return False

def process_all_images():
    """Process all images in the input folder with multiple enhancement techniques"""
    # Ensure output directory exists
    create_dir(OUTPUT_FOLDER)
    
    # Get list of image files
    image_files = [f for f in os.listdir(INPUT_FOLDER) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    if not image_files:
        print(f"No image files found in {INPUT_FOLDER}")
        return
    
    print(f"Found {len(image_files)} images to process")
    
    # Process each image
    for filename in image_files:
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        temp_path = os.path.join(OUTPUT_FOLDER, "temp_" + filename)
        
        try:
            print(f"Processing {filename}...")
            
            # Step 1: Sharpen with OpenCV
            if sharpen_image_cv2(input_path, temp_path):
                # Step 2: Denoise the sharpened image
                if denoise_image(temp_path, output_path):
                    print(f"✅ Successfully enhanced {filename}")
                    # Remove temporary file
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                else:
                    # If denoising fails, use the sharpened image
                    os.rename(temp_path, output_path)
                    print(f"✅ Successfully sharpened {filename} (denoising skipped)")
            else:
                # Fallback to PIL if OpenCV method fails
                print(f"OpenCV enhancement failed for {filename}, trying PIL method...")
                if enhance_image_pil(input_path, output_path):
                    print(f"✅ Successfully enhanced {filename} with PIL")
                else:
                    print(f"❌ Failed to enhance {filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            # Clean up any temporary files
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    print(f"\nImage enhancement complete!")
    print(f"Enhanced images saved to: {OUTPUT_FOLDER}")

if __name__ == "__main__":
    print("Starting image enhancement process...")
    process_all_images()