import os
import shutil

# Specify the number of folders and images per folder
num_folders = 5
images_per_folder = 5

# Create a directory to hold the folders
output_dir = "image_folders"
os.makedirs(output_dir, exist_ok=True)

# Loop through each folder
for folder_num in range(1, num_folders + 1):
    folder_name = os.path.join(output_dir, f"folder{folder_num}")
    os.makedirs(folder_name, exist_ok=True)
    
    # Loop to create and copy image files with sequential names
    for image_num in range(1, images_per_folder + 1):
        # Generate a sequential image file name
        image_name = f"image_{image_num}.jpg"  # You can change the extension if needed
        
        # Create a sample image file (you should replace this with actual image copying)
        # In this example, we'll create an empty image file
        with open(os.path.join(folder_name, image_name), "wb") as f:
            pass

print(f"Created {num_folders} folders, each containing {images_per_folder} sequentially named image files.")
