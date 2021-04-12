#!/usr/bin/env python3

from PIL import Image

Image.open('fish.png').convert('RGB').save('output.png')

# actf{in_the_m0rning_laughing_h4ppy_fish_heads_in_th3_evening_float1ng_in_your_soup}
