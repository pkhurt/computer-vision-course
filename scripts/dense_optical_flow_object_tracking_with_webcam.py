

import cv2
import numpy as np

def dense_optical_flow_object_tracking_with_webcam():
    """
    Perform dense optical flow object tracking using the webcam.

    This function captures frames from the webcam, calculates the optical flow
    between consecutive frames, and displays the flow vectors as colors on the
    screen.

    Observeration: The flow vectors are calculated for each pixel in the frame. 
    The direction of the flow is represented by the hue of the color. That means if the
    camera video starts and a person moves from left to right, the color of the flow vector 
    appears in a certain color. Same if the object moves from right to left the color should be
    a different one but stay more or less the same. With that one can track / identify multiple 
    objects in the video stream.

    Returns:
        None
    """

    cap = cv2.VideoCapture(0)

    ret, frame1 = cap.read()

    prvsImg = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    hsv_mask = np.zeros_like(frame1)
    hsv_mask[:,:,1] = 255

    while True:
        ret, frame2 = cap.read()
        nextImg = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prvsImg, nextImg, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # flow contains the flow vectors for each pixel
        # it is a 2d array with the same size as the input image

        mag, ang = cv2.cartToPolar(flow[:,:,0], flow[:,:,1], angleInDegrees=True) # magnitude and angle from vertical and horizontal information

        hsv_mask[:,:,0] = ang/2 # that way we can see the direction of the flow and see the angle from 0 to 180

        hsv_mask[:,:,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX) # actual value defined by the actual magnitude

        bgr = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
        cv2.imshow("frame", bgr)

        k = cv2.waitKey(10) & 0xFF
        if k == 27: # esc key
            break

        prvsImg = nextImg # update the previous image

    cap.release()
    cv2.destroyAllWindows()

dense_optical_flow_object_tracking_with_webcam()
