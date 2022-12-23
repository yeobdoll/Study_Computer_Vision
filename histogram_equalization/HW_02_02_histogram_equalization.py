import os
import cv2
from matplotlib import pyplot as plt

# Set the working directory to be the current one
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load a color image
img_original = cv2.imread('lena.jpg')

# 이미지를 채널별로 분리
img_b, img_g, img_r = cv2.split(img_original)

# 각 채널의 히스토그램을 균일화 한다.
img_equalized_r = cv2.equalizeHist(img_r)
img_equalized_g = cv2.equalizeHist(img_g)
img_equalized_b = cv2.equalizeHist(img_b)

# 균일화된 채널을 병합한다.
img_merge = cv2.merge((img_equalized_r, img_equalized_g, img_equalized_b))

# Calculate histograms
hist_original = cv2.calcHist([img_original], [0], None, [256], [0,256])
hist_equalized = cv2.calcHist([img_merge], [0], None, [256], [0,256])

# Cummulative histograms
cum_hist_original = hist_original.cumsum()
cum_hist_equalized = hist_equalized.cumsum()

plt.figure(figsize=(10, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)), plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(222)
for i, col in enumerate(['b','g','r']):
    hist = cv2.calcHist([img_original], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
    plt.title('histogram')

plt.subplot(223)
plt.imshow(img_merge), plt.xticks([]), plt.title('equalized'), plt.yticks([])

plt.subplot(224)
for i, col in enumerate(['b','g','r']):
    hist = cv2.calcHist([img_merge], [i], None, [256], [0, 256])
    cum_hist = hist.cumsum()
    plt.plot(cum_hist, color = col)
    plt.xlim([0, 256])
    plt.title('cumulative histogram after equalization')

# plt.savefig('HW_02_02_histogram_equalization.png')
plt.show()

