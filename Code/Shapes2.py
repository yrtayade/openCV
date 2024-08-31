import cv2 as cv
import numpy as np

blank = np.zeros( (500,500),dtype = np.uint8  )
# blank = cv.imread("../cat.jpeg")

# cv.rectangle(img=blank, pt1=(100,100),pt2=(300,300), color=(255,0,0), thickness=3)

# cv.line(img=blank, pt1=(100,100),pt2=(300,300), color=(255,0,0), thickness=3)

# cv.circle(img=blank, center=(200,200),radius=100, color=(0,255,0), thickness=-1)

def drawing(event,x,y,flag,param):
    if flag==1:
        cv.circle(img=blank, center=(x,y),radius=3, color=(255,0,0), thickness=-1)

cv.namedWindow("myBoard")
cv.setMouseCallback("myBoard",drawing)

while True:
    cv.imshow("myBoard",blank)
    if cv.waitKey(1) & 0xFF ==ord('d'):
        break