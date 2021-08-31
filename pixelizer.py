from PIL import Image
import sys
import os


def pixelizer(input, output):
  input_path = './png/raw/'
  output_path = './png/pixelized/'
  os.mkdir(input_path)
  os.mkdir(output_path)

  image = Image.open(input_path+input)
  downscaled_image = image.resize((image.size[0]/pixel_size, image.size[1]/pixel_size),Image.NEAREST)
  upscaled_image = downscaled_image.resize((downscaled_image.size[0]*pixel_size*scale, downscaled_image.size[1]*pixel_size*scale), Image.NEAREST)
  upscaled_image.save(output_path+output)
