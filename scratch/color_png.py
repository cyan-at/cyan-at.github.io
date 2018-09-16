#!/usr/bin/env python

# Unpublished Copyright (c) 2018 CYAN, All Rights Reserved.

import argparse

import numpy as np
from PIL import Image

def hex_to_rgb(value, out_of_255=True):
    value = value.lstrip('#')
    lv = len(value)
    # '/ 255.0' for GL -> floats instead of out of 255
    if (out_of_255):
        return tuple(int(value[i:i + lv // 3], 16) / 255.0 for i in range(0, lv, lv // 3))
    else:
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

parser = argparse.ArgumentParser(description="change the color of various icons")
parser.add_argument('--png_file_i', type=str, required=True, help='i png image') # abs path
parser.add_argument('--filter_rgb', type=str, default='-1,-1,-1', help='to_filter_rgb , delimited')
parser.add_argument('--to_hex', type=str, required=True, help='target hex')
parser.add_argument('--png_file_o', type=str, required=True, help='o png image') # abs path
args = parser.parse_args()

im = Image.open(args.png_file_i)
data = np.array(im)
red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]

# r1, g1, b1 = 0, 0, 0 # Original value, black
filter_rgb = map(lambda x: int(x), args.filter_rgb.strip().split(","))
valid_rgb_values = reduce(
	lambda a, b: a and b, map(lambda x: x >= 0 and x <= 255, filter_rgb))

if len(filter_rgb) == 3 and valid_rgb_values:
	mask = (red == filter_rgb[0]) & (green == filter_rgb[1]) & (blue == filter_rgb[2])
else:
	mask = (red >= 0) & (green >= 0) & (blue >= 0) # effectively no mask

rgb = hex_to_rgb(args.to_hex, False)
r2, g2, b2 = rgb[0], rgb[1], rgb[2] # Value that we want to replace it with

data[:,:,:3][mask] = [r2, g2, b2]

im = Image.fromarray(data)
im.save(args.png_file_o)