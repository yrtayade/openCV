import cv2 as cv
import numpy as np

image = cv.imread("group-1.jpg")
cv.imshow("original_image", image)
cropped_image = image[10:100, 20:200]
cv.imshow("cropped_image", cropped_image)
image[30:100, 50:200] = cropped_image
cv.imshow("original_image", image)
cv.waitKey(0)