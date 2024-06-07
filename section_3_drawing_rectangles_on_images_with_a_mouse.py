import cv2
import numpy as np

# Variables
drawing = False  # will be true while muouse button down, false while mouse button up
ix, iy = -1, -1

##############
## Function ##
##############

def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing # makes them changeable in this function
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x, y), (0, 255, 0), -1)


####################################
## Showing the image with open cv ##
####################################
# Black
cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_rectangle)

img = np.zeros((512,512,3), np.int8)

while True:
    cv2.imshow("my_drawing", img)



    # checks for esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()