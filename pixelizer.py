from PIL import Image
import os

def run(input, output):
    pixel_size = 5
    scale = 1

    output_path = './png/pixelized/'
    if os.path.exists(output_path):
        print('''Folder './png' exists''')
    else:
        print('''Creating folder './png' ''')
        os.mkdir(output_path)

    image = Image.open(input)
    downscaled_image = image.resize((int(image.size[0] / pixel_size), int(image.size[1] / pixel_size)), Image.NEAREST)
    upscaled_image = downscaled_image.resize(
        (downscaled_image.size[0] * pixel_size * scale, downscaled_image.size[1] * pixel_size * scale), Image.NEAREST)
    upscaled_image.save(output_path + output)
