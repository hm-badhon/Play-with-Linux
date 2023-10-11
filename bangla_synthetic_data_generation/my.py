from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import random
import os

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    """
    Add salt and pepper noise to the input image.

    Args:
        image (PIL.Image): Input image.
        salt_prob (float): Probability of adding salt noise.
        pepper_prob (float): Probability of adding pepper noise.

    Returns:
        PIL.Image: Image with salt and pepper noise.
    """
    image = np.array(image)
    noisy_image = np.copy(image)

    # Add salt noise
    salt = int(image.size * salt_prob)
    salt_coords = [random.randint(0, image.shape[0] - 1) for _ in range(salt)]
    pepper_coords = [random.randint(0, image.shape[0] - 1) for _ in range(int(image.size * pepper_prob))]
    noisy_image[salt_coords] = 255

    # Add pepper noise
    pepper = int(image.size * pepper_prob)
    noisy_image[pepper_coords] = 0

    return Image.fromarray(noisy_image)

def generate_text_image(text, font_path, image_size, salt_prob, pepper_prob):
    """
    Generate a synthetic text image with added noise.

    Args:
        text (str): Text to be rendered on the image.
        font_path (str): Path to the TrueType font file.
        image_size (tuple): Size of the image (width, height).
        salt_prob (float): Probability of adding salt noise.
        pepper_prob (float): Probability of adding pepper noise.

    Returns:
        PIL.Image: Synthetic text image with added noise.
    """
    # Create a blank image
    image = Image.new('L', image_size, color=255)
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, size=32)

    # Calculate text position
    text_width, text_height = draw.textsize(text, font)
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=0)

    # Add salt and pepper noise
    noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

    return noisy_image

if __name__ == "__main__":
    root = "dataset"
    if not os.path.exists(root):
        os.makedirs(root)

    input_path = "data_b"
    if not os.path.exists(os.path.join(root, input_path)):
        os.makedirs(os.path.join(root, input_path))

    with open("words.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()

    for word in words:
        image_name = f"original_{word}.png"
        text = word
        font_path = "fonts/alponalohit/AponaLohit.ttf"  # Ensure the correct font path
        image_size = (400, 100)  # Adjust the image size as needed
        salt_prob = 0.005
        pepper_prob = 0.005

        image = generate_text_image(text, font_path, image_size, salt_prob, pepper_prob)
        image.save(os.path.join(root, input_path, image_name))

        # Optionally, you can save the image-label pair to a text file or a JSON file.
