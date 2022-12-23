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
        theta += 10 
        change += 10
        rad_change = math.radians(change)
        cv2.destroyAllWindows()
        M = cv2.getRotationMatrix2D((w/2,h/2), theta, 1)

        print(M) 
        nw = abs(w * np.cos(rad_change)) + abs(h * np.sin(rad_change))
        nh = abs(w * np.sin(rad_change)) + abs(h * np.cos(rad_change))
        M2 = np.float32([[0, 0, nw/2 - w/2],
                        [0, 0, nh/2 - h/2]])   
        M3 = M + M2     
        img_res = cv2.warpAffine(img_orig, M3, (int(nw), int(nh)))
        cv2.imshow('',img_res) 
        if change == 350: 
            break
    elif key == 27:
        break

cv2.destroyAllWindows()