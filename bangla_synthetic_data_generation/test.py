from PIL import ImageFont, ImageDraw, Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random
import json
import os
import glob


def sp_noise(image, prob_salt, prob_pepper):
    '''
    Add salt and pepper noise to the image.
    prob_salt: Probability of adding salt noise
    prob_pepper: Probability of adding pepper noise
    '''
    output = np.zeros(image.shape, np.uint8)
    thres_salt = 1 - prob_salt
    thres_pepper = prob_pepper
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob_salt:
                output[i][j] = 0
            elif rdn > thres_salt:
                output[i][j] = 220
            else:
                output[i][j] = image[i][j]
    image = cv2.GaussianBlur(output, (3, 3), 20)
    return image

def DataGenerator(root, img_dir, data):
    # input_text = "1205 4789 8748 57812"

    for i in data.split(" "):
        print(i)
        input_text = i
        if len(input_text) > 10:
            width = 450
        else:
            width = 200
        image = np.zeros((60, width, 3), np.uint8)
        image = sp_noise(image, 0.005, 0.05)
        pil_im = Image.fromarray(image)
        draw = ImageDraw.Draw(pil_im)
        # font_path = "fonts/AbuBakarD_unicode/ABUBKARKACHUAD3BoldItalic.ttf"
        # font_path = "fonts/AbuBakarD_unicode/Bitopi_Unicode/Bitopi_Unicode/Bitopi_Unicode-bengalifont.com/BitopiBijoy.ttf"
        font_path="fonts"
        font_path_list = glob.glob(font_path+"/*")
        for font_path in font_path_list:

            # Ensure the correct font path
            font = ImageFont.truetype(font_path, 32)
            draw.text((1, 1), input_text, font=font)
            cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
            image = sp_noise(cv2_im_processed, 0.05, 0.05)
            image = 255 - image
            image_name = f"original_{i}_{os.path.basename(font_path)}.png"
            
            original = os.path.join(root, img_dir, image_name)
            cv2.imwrite(original, image)
        return image_name, input_text

if __name__ == "__main__":
    data_str = "রওশন এরশাদ​ আবারও জাতীয় পার্টিতে (জাপা) জি এম কাদের ও রওশন এরশাদের মধ্যে ক্ষমতার দ্বন্দ্ব দেখা দিয়েছে।"
    root = "dataset"
    if not os.path.isdir(root):
        os.makedirs(root)
    input_path = "data"
    if not os.path.isdir(os.path.join(root, input_path)):
        os.makedirs(os.path.join(root, input_path))
    data_list = []
    txt_file = open("bn_annotation.txt", "w")
    # with open(".txt", "r") as f:
    #     data = f.read()
    x = data_str.split(" ")
    for i in x[:1]:
        bn_word = i.split("|")[-1]
        img_dir, text = DataGenerator(root, input_path, bn_word)
        if text == "\u200c" or text == "\u200d":
            continue
        # txt_file.write(img_dir + " " + text + "\n")
        data_list.append(bn_word)
    # txt_file.close()
    max_string = max(data_list, key=len)
    print("max string:", len(max_string))
