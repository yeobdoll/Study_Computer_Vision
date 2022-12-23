import os
import cv2

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a reference image as grayscale
img_orig = cv2.imread('fish.png', 0)
rows,cols = img_orig.shape
cv2.imshow('',img_orig)

theta = 0
while True:
    key = cv2.waitKey(0)
    if key == 32:
        theta += 10
        cv2.destroyAllWindows()
        M = cv2.getRotationMatrix2D((cols/2,rows/2), theta, 1)
        # print(M)
        img_res = cv2.warpAffine(img_orig, M, (cols,rows))
        cv2.imshow('',img_res)
        # print(theta)
        if theta == 350:
            break
    elif key == 27:
        break   
cv2.destroyAllWindows() 