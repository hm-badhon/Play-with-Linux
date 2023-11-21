import filecmp
import os

def compare_folders(folder1_path, folder2_path):
    # Compare the two folders
    dcmp = filecmp.dircmp(folder1_path, folder2_path)

    # Check if the common files are identical
    if not dcmp.diff_files and not dcmp.left_only and not dcmp.right_only:
        print("Folders are identical.")
    else:
        print("Folders are different.")

        # Print the differing files
        for diff_file in dcmp.diff_files:
            print(f"Differing file: {diff_file}")

        # Print files only in the first folder
        for left_only_file in dcmp.left_only:
            print(f"File only in {folder1_path}: {left_only_file}")

        # Print files only in the second folder
        for right_only_file in dcmp.right_only:
            print(f"File only in {folder2_path}: {right_only_file}")

# Example usage
folder1_path = 'badhon2'
folder2_path = 'badhon2'
compare_folders(folder1_path, folder2_path)
