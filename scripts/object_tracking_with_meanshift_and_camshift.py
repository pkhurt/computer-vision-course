import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# setup initial location of window
# Face detection: We will first setup the initial location of the 
# window to the location of the face in the first frame. This will be tracked.
face_cascade = cv2.CascadeClassifier('trained_models/haarcascade_frontalface_default.xml')
face_rects = face_cascade.detectMultiScale(frame) # Returns rectangles of faces in the frame

(face_x, face_y, width, height) = tuple(face_rects[0]) # first face rectangle
track_window = (face_x, face_y, width, height)

# Now we want to track the face the rest of the video using meanshift
# set up the ROI for tracking
roi = frame[face_y:face_y+height, face_x:face_x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) # convert to HSV
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180]) # calculate histogram to backproject the target to the frame in order to calculate mean shift
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) # termination criteria either 10 iterations or move by at least 1 pt

while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1) # backproject the target to the frame
        
        ##### Resize the window if the face changes the distance #####
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, (0, 255, 0), 5)
        #####
        
        cv2.imshow('img', img2)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    else:
        break

cv2.destroyAllWindows()
cap.release()