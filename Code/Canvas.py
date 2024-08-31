import cv2 as cv
import numpy as np

blank_sheet = np.zeros( (512,512,3), dtype = np.uint8)
drawing  = False
color = (0,0,0)

def mouse_callback(event, x, y, flags, param):
    global drawing , color

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(blank_sheet, (x, y), 5, color, -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
    
cv.namedWindow('Paint')
cv.setMouseCallback('Paint',mouse_callback)

while True:
    cv.imshow('Paint',blank_sheet)
    key = cv.waitKey(1) & 0xFF
    if key == ord('r'):
        color = (0,0,255)
    elif key == ord('g'):
        color = (0,255,0)
    elif key == ord('b'):
        color = (255,0,0)
    elif key == ord('e'):
        color = (0,0,0)
    elif key == 27:
        break

cv.destroyAllWindows()