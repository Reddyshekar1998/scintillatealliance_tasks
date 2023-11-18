from PIL import Image
import pytesseract
import os
import re

path = "/home/reddy/Documents/python_coding_task/screen_shots"
for image_name in os.listdir(path):
    image_path = os.path.join(path, image_name)
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    price = re.search(r'\$(\d+)',text)
    if price:
        price = price.group().split('$')[-1]
    else:
        price = None
    ratings = re.search(r'(\d+)\s+ratings',text)
    if ratings:
        ratings = ratings.group()
    else:
        ratings = None
    print(price)
    print(ratings)

