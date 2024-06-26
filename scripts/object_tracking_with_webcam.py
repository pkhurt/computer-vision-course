import numpy as np
import cv2

corner_track_params = dict(maxCorners=20, qualityLevel=0.02, minDistance=20, mask=None, blockSize=3, useHarrisDetector=False, k=0.1)

# larger motions can be detected by larger winsize but it is more sensitive to noise
# maxLevel is based on pyarmid for image processing: https://en.wikipedia.org/wiki/Pyramid_(image_processing) 
# criteria we use both, speed (count) vs. accuracy of the algorithm (eps)
lucas_kanade_params = dict(winSize=(200,200), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) 

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# # Points to track
prev_points = cv2.goodFeaturesToTrack(prev_gray, **corner_track_params)

mask = np.zeros_like(prev_frame) # visualization - zeros with the same size of the prev_frame

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # calculating the optical flow on the actual frame
    next_points, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prev_points, None, **lucas_kanade_params)

    good_new = next_points[status==1]
    good_prev = prev_points[status==1]

    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel() # reshape / flattening out an array -> 2d to 1d
        x_prev, y_prev = prev.ravel()

        mask = cv2.line(mask, (int(x_new), int(y_new)), (int(x_prev), int(y_prev)), (0,255,0), 3)
        frame = cv2.circle(frame, (int(x_new), int(y_new)), 8, (0,0,255), -1)
    img = cv2.add(frame, mask)
    cv2.imshow("tracking", img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

    prev_gray = frame_gray.copy()

    prev_points = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()

    