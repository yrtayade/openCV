import cv2
import numpy as np

# Initialize the canvas
canvas = np.zeros((512, 512, 3), dtype=np.uint8)
drawing = False  # True if the mouse is pressed
color = (0, 0, 0)  # Default color is black

def mouse_callback(event, x, y, flags, param):
    global drawing, color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas, (x, y), 5, color, -1)  # Draw a filled circle
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Create a window and set up the mouse callback
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', mouse_callback)

while True:
    cv2.imshow('Paint', canvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):  # Change color to red
        color = (0, 0, 255)
    elif key == ord('g'):  # Change color to green
        color = (0, 255, 0)
    elif key == ord('b'):  # Change color to blue
        color = (255, 0, 0)
    elif key == 27:  # Press 'ESC' to exit
        break
cv2.destroyAllWindows()
