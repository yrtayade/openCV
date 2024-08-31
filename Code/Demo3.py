import cv2 as cv
import numpy as np
xs = -1 
ys=-1
xe = -1
ye= -1
shape = False
draw = False
myColor = (255,255,255)
blank_sheet  = cv.imread('../cat.jpeg')
def drawing(event, x, y, flag, param):
    global draw, myColor, shape, xs,ys,xe,ye
    if shape == True:
        if shape == True and event == cv.EVENT_LBUTTONDOWN:
            xs = x
            ys = y        
        if shape == True and event == cv.EVENT_LBUTTONUP:
            xe = x
            ye = y
            cv.circle(blank_sheet, radius=0, center=(x,y), thickness=0, color=myColor)
            cv.rectangle(img = blank_sheet, pt1=(xs,ys), pt2=(xe,ye),color=myColor, thickness=1)

            newImg = blank_sheet[ xs:ys , xe:ye]
            cv.imshow("new cropped Image",newImg)
    else:
        if event == cv.EVENT_LBUTTONDOWN:
            draw = True
            print("Drawing start")
        if draw == True:
            cv.circle(blank_sheet, radius=10, center=(x,y), thickness=5, color=myColor)
        if event == cv.EVENT_LBUTTONUP:
            draw = False
            print("Drawing Stopped")

cv.namedWindow('Paint')
cv.setMouseCallback('Paint', drawing )

while True:
    cv.imshow('Paint', blank_sheet)
    # cv.rectangle(img=blank_sheet, pt1=(100,100),pt2=(300,300),color=(255,23,120), thickness=-1)
    key = cv.waitKey(1) & 0xFF
    if key == ord('r'):
        myColor = (0,0,255)
    if key == ord('g'):
        myColor = (0,255,0)
    if key == ord('b'):
        myColor = (255,0,0)
    if key == ord('e'):
        myColor = (0,0,0)
    if key == ord('s'):        
        shape = True
    if key == 27:
        break
cv.destroyAllWindows()