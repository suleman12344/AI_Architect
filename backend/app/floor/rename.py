import os

# Folder containing the images
folder_path = 'backend/app/2d_floor_/images'

# New base name for files
base_name = 'image'

# Supported image extensions
extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

# Loop through files and rename
for count, filename in enumerate(os.listdir(folder_path)):
    if filename.lower().endswith(extensions):
        ext = os.path.splitext(filename)[1]
        new_name = f"{base_name}_{count + 1}{ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)

print("Renaming complete!")
