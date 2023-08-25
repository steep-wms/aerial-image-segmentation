#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
from samgeo import SamGeo

if len(sys.argv) != 3:
    print("Usage: python3 segment.py <input_image> <output_image>")
    exit(1)

sam = SamGeo(checkpoint='sam_vit_b_01ec64.pth')
sam.generate(sys.argv[1])
sam.save_masks()

plt.imsave(sys.argv[2], sam.objects, cmap='Blues')
