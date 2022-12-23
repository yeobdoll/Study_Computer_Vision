import cv2
import os
import cv2

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load grayscale images
img_orig = cv2.imread('baboon.jpg')

# Create a window
winname = 'Morphology'
cv2.namedWindow(winname)

# mode 
Morphology_Tpye = {0: 'erode', 1: 'dilate', 2: 'open', 3: 'close', 4: 'tophat', 5: 'blackhat', 6:'gradient'}
Kernel_Shape = {0: 'rect', 1: 'cross', 2: 'ellipse'}

# Trackbar callback function
def do(x):
    Type = cv2.getTrackbarPos('Type', winname)
    Shape = cv2.getTrackbarPos('Shape', winname)
    Size = cv2.getTrackbarPos('Size', winname)
    Iterations = cv2.getTrackbarPos('Iterations', winname)

    kernel = cv2.getStructuringElement(Shape, (2 * Size + 1, 2 * Size + 1))
    mopping_img = cv2.morphologyEx(img_orig, Type, kernel, iterations=Iterations)

    # 3 5 7 9 11 13
    if Size == 0:
        size = 3 + Size # 3
    elif Size == 1:
        size = 4 + Size # 5
    elif Size == 2:
        size = 5 + Size # 7
    elif Size == 3:
        size = 6 + Size # 9
    elif Size == 4:
        size = 7 + Size # 11
    elif Size == 5:
        size = 8 + Size # 11

    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(mopping_img, "Morphology Type: {}".format(Morphology_Tpye[Type]), (10,40), font, 0.4, (255,255,255), 1)
    cv2.putText(mopping_img, "Kernel Shape : {}".format(Kernel_Shape[Shape]), (10,60), font, 0.4, (255,255,255), 1)
    cv2.putText(mopping_img, "Kernel Size: {}".format(size), (10,80), font, 0.4, (255,255,255), 1)
    cv2.putText(mopping_img, "Iterations: {}".format(Iterations), (10,100), font, 0.4, (255,255,255), 1)

    cv2.imshow(winname, mopping_img)
# Create trackbars for color change
cv2.createTrackbar('Type', winname, 0, 6, do)
cv2.createTrackbar('Shape', winname, 0, 2, do)
cv2.createTrackbar('Size', winname, 0, 5, do)
cv2.createTrackbar('Iterations', winname, 0, 10, do)

do(0)
cv2.waitKey(0)