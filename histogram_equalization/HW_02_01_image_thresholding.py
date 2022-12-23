import os
import cv2
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img = cv2.imread('opencv-logo-white.png')
# 이미지를 채널별로 분리
img_b, img_g, img_r = cv2.split(img)

# # 각 채널 thresholding
thld = 127
max_v = 255
ret, img1 = cv2.threshold(img_r, 127, max_v, cv2.THRESH_BINARY)
ret, img2 = cv2.threshold(img_g, 127, max_v, cv2.THRESH_BINARY)
ret, img3 = cv2.threshold(img_b, 127, max_v, cv2.THRESH_BINARY)

# bit-wise AND 연산 수행
bwA_12 = cv2.bitwise_and(img1, img2)
bwA_result = cv2.bitwise_and(bwA_12, img3)

# # Display results
titles = ['original','R','G','B', 'result']
images = [img, img1, img2, img3, bwA_result]

for i in range(5):
    plt.subplot(1,5, i+1)
    plt.imshow(images[i], 'gray' ,vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    # plt.savefig('HW_02_01_image_thresholding.png')
plt.show()

