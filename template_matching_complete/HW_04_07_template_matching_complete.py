import os
import cv2
import numpy as np
import math

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('fish.png', cv2.IMREAD_GRAYSCALE)
img_test01 = cv2.imread('test_1.png', 0)
img_test02 = cv2.imread('test_2.png', 0)
img_test03 = cv2.imread('test_3.png', 0)
h, w = img_orig.shape
# print(h, w)

img_mask = img_orig.copy()
# rows, cols = img_mask.shape
img_mask[:] = 255
# img_mask[0, :] = 0
# img_mask[:, 0] = 0
# img_mask[rows-1, :] = 0
# img_mask[:, cols-1] = 0

img_orig= cv2.adaptiveThreshold(img_orig, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5) 

scale = [0.5, 1, 1.5]
theta = range(0, 360, 10)
img_list = [img_test01, img_test02, img_test03]

for reference in img_list:
    for sc in scale:
        for th in theta:
            # print(th)
            nh = abs(w*math.sin(math.radians(th))) + abs(h*math.cos(math.radians(th)))
            nw = abs(w*math.cos(math.radians(th))) + abs(h*math.sin(math.radians(th)))   

            M = cv2.getRotationMatrix2D((w/2 , h/2), th, 1)    
            M2 = np.float32([[0, 0, nw/2 - w/2], [0, 0, nh/2-h/2]])   
            M3 = M + M2     

            img_res = cv2.warpAffine(img_orig, M3, (int(nw), int(nh)))
            img_mask_res = cv2.warpAffine(img_mask, M3, (int(nw), int(nh)))

            img_res = cv2.resize(img_res, None, fx=sc, fy=sc, interpolation=cv2.INTER_CUBIC)
            img_mask_res = cv2.resize(img_mask_res, None, fx=sc, fy=sc, interpolation=cv2.INTER_CUBIC)

            res = cv2.matchTemplate(reference, img_res, cv2.TM_CCORR_NORMED, mask=img_mask_res)
            
            # Threshold value
            threshold = 0.94
            loc = np.where(res >= threshold)

            # Draw red box
            img_reference = cv2.cvtColor(reference, cv2.COLOR_GRAY2BGR)

            w2, h2 = img_res.shape[::-1]
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_reference, pt, (pt[0] + w2, pt[1] + h2), (0,0,255), 2)

            if len(loc[0]) != 0:
                cv2.imshow('result', img_reference)
            key = cv2.waitKey(0)    
            cv2.destroyAllWindows()

            if key == 27: break
        if key == 27: break
    if key == 27: break                