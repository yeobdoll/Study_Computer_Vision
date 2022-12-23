import os
import cv2
import numpy as np
import math

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('fish.png', 0)
h, w = img_orig.shape
cv2.imshow('',img_orig)
# Translation
theta = 0
change = 0

while True:
    key = cv2.waitKey()
    if key == 32:   
        # theta += 10 
        change += 10
        rad_change = math.radians(change)
        cv2.destroyAllWindows()
        nw = abs(w * np.cos(rad_change)) + abs(h * np.sin(rad_change))
        nh = abs(w * np.sin(rad_change)) + abs(h * np.cos(rad_change))

        # M = cv2.getRotationMatrix2D((cols/2,rows/2), theta, 1)
        print(change)
        print(nw, nh)
        M = np.float32([[1, 0, nw/2 - w/2], 
                        [0, 1, nh/2 - h/2]])
        print(M)
        img_res = cv2.warpAffine(img_orig, M, (int(nw), int(nh)))
        cv2.imshow('',img_res) 
        if change == 350: 
            break
    elif key == 27:
        break

cv2.destroyAllWindows()