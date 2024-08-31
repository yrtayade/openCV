import numpy as np
import cv2 as cv
# mouse callback function
start = False
x1= 0
x2= 0
y1= 0
y2 = 0
def drawfunction(event,x,y,flags,param):
    global start,x1,x2,y1,y2
    if event == cv.EVENT_LBUTTONDOWN:
        x1,y1 = x,y
    if event == cv.EVENT_LBUTTONUP:        
        x2,y2 = x,y
        cv.rectangle(img,pt1=(x1,y1),pt2=(x2,y2),color=(255,0,0,),thickness=1)
img = cv.imread('../cat.jpeg')
print( img )
cv.namedWindow('image')
cv.setMouseCallback('image',drawfunction)
while(1):
   cv.imshow('image',img)
   key=cv.waitKey(1)
   if key == 27:
      break
cv.destroyAllWindows()