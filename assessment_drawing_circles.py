import cv2
import numpy as np

def draw_circle(event, x, y, flags, params):
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0),-1)
    

cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_circle)

img = np.zeros((512,512,3), np.int8)

while True:
    cv2.imshow("drawing", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()