# Image Negative
# s = L-1, L-1 = 255 for 8bit image.
import cv2
import numpy as np

def image_negative(img):  
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = np.max(img) - img[i][j]
    return img

img = cv2.imread("1.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

negative = image_negative(img.copy())
grayNegative = image_negative(gray.copy())

cv2.imshow("negative",negative)
cv2.imshow("gray negative",grayNegative)
cv2.imshow("gray",gray)
cv2.imshow("frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)