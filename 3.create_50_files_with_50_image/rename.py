import os

# Specify the directory containing the folders with image files
base_directory = "image_folders"

# Loop through each folder
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    
    if os.path.isdir(folder_path):
        # Get a list of image files within the folder
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        
        # Sort the image files to ensure sequential renaming
        image_files.sort()
        
        # Rename the image files sequentially
        for i, image_file in enumerate(image_files, start=1):
            extension = os.path.splitext(image_file)[1]
            new_name = f"{folder_name}_{i}{extension}"
            old_path = os.path.join(folder_path, image_file)
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the image file
            os.rename(old_path, new_path)

print(f"Renamed all image files within the folders.")

