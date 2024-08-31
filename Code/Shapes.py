import cv2 as cv
import numpy as np
img = np.zeros((500,500),np.uint8)
def myEvent(event, x,y, flag, param):
    global img
    if event == cv.EVENT_LBUTTONDBLCLK:
        img = np.zeros((500,500),np.uint8)        
    cv.circle(img,center=(x,y),radius=5, color=(255,0,0),thickness=-1 )

cv.namedWindow("myImage")
cv.setMouseCallback( "myImage", myEvent )

while True:
    cv.imshow("myImage", img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
cv.destroyAllWindows()

# img = cv.imread("../cat.jpeg")
# cv.imshow("myImage", img)
# # new_img = cv.resize(img, (500,500))
# # cv.imshow("myImage2", new_img)

# cropped_image = img[80:280, 150:330]
 
# cv.imshow("cropped", cropped_image)
#Example 
# blank =  np.zeros( (500 , 500),dtype=np.uint8  )
# cv.rectangle(img=blank, pt1=(100,100), pt2=(300,300),color=(255,0,0), thickness=3)
# cv.circle(img=blank,center=(300,300),radius=50,color=(255,10,10), thickness=2 )


#Example2
# cv.line(img=blank, pt1=(50,50),pt2=(100,50),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(70,70),pt2=(120,70),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(50,50),pt2=(70,70),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(100,50),pt2=(120,70),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(50,50),pt2=(10,70),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(10,70),pt2=(10,150),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(70,70),pt2=(70,150),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(120,70),pt2=(120,150),color=(255,0,0), thickness=2)
# cv.line(img=blank, pt1=(10,150),pt2=(120,150),color=(255,0,0), thickness=2)
# cv.imshow("", blank)
# cv.waitKey(0)