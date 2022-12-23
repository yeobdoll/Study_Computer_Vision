import os
import cv2
import numpy as np
import math

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('fish.png', 0)
img_mask = img_orig.copy()
cols, rows = img_mask.shape
img_mask[:] = 255
img_mask[0, :] = 0
img_mask[:, 0] = 0
img_mask[cols-1, :] = 0
img_mask[:, rows-1] = 0

h, w = img_orig.shape
# Translation
change = 0
scale = [0.5, 1.0, 1.5]
theta = range(0, 360, 10)

for i in scale:
    for k in theta: 
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        img_resize = cv2.resize(img_mask, None, fx=i, fy=i, interpolation=cv2.INTER_CUBIC)
        cv2.imshow('', img_resize) 
        if key == 32:
            change += 10
            rad_change = math.radians(change) 
            M = cv2.getRotationMatrix2D((w/2,h/2), k, 1)    
            nw = abs(w * np.cos(rad_change)) + abs(h * np.sin(rad_change))
            nh = abs(w * np.sin(rad_change)) + abs(h * np.cos(rad_change))
            M2 = np.float32([[0, 0, nw/2 - w/2],
                            [0, 0, nh/2 - h/2]])   
            M3 = M + M2     
            img_res = cv2.warpAffine(img_mask, M3, (int(nw), int(nh)))
            img_res = cv2.resize(img_res, None, fx=i, fy=i, interpolation=cv2.INTER_CUBIC)  
            print(change)
            cv2.imshow('',img_res)                                                                                   
            if change == 350: 
                break
        if key == 27: break
    if key == 27: break      

cv2.destroyAllWindows()