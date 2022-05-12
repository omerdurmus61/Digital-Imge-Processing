# Image Negative
# s = L-1, L-1 = 255 for 8bit image.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("1.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

negative = np.max(img) - img.copy()
grayNegative = np.max(gray) - gray.copy()

plt.subplot(2,2,1)
plt.imshow(gray,cmap="gray")
plt.title("Gray")

plt.subplot(2,2,2)
plt.imshow(grayNegative,cmap="gray")
plt.title("Negative")

plt.subplot(2,2,3)
plt.imshow(img,cmap="gray")
plt.title("Negative")

plt.subplot(2,2,4)
plt.imshow(negative)
plt.title("Negative")

plt.show()

