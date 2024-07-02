import numpy as np
import cv2
import argparse


def parse() -> str:
    parser = argparse.ArgumentParser(description="Use different Tracker APIs to track an object in the webcam video.")
    parser.add_argument("--Boosting", help="Use the Boosting tracker", action="store_true")
    parser.add_argument("--MIL", help="Use the MIL tracker", action="store_true")
    parser.add_argument("--KCF",  help="Use the KCF tracker", action="store_true")
    parser.add_argument("--TLD", help="Use the TLD tracker", action="store_true")
    parser.add_argument("--MedianFlow", help="Use the MedianFlow tracker", action="store_true")

    args = parser.parse_args()

    if args.Boosting:
        return cv2.TrackerBoosting_create()
    elif args.MIL:
        return cv2.TrackerMIL_create()
    elif args.KCF:
        return cv2.TrackerKCF_create()
    elif args.TLD:
        return cv2.TrackerTLD_create()
    elif args.MedianFlow:
        return cv2.TrackerMedianFlow_create()
    else:
        raise Exception("Please specify a tracker to use")
    
def start_tracking(tracker):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    roi = cv2.selectROI(frame, False) # draw manually the region that we want to track
    ret=tracker.init(frame, roi)

    while True:
        ret, frame = cap.read()
        if ret == True:
            success, roi = tracker.update(frame) # success will be false if the tracker fails to track the object (for example object left the frame)
            (x,y,w,h) = tuple(map(int, roi))

            if success:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
                cv2.imshow('img', frame)
            else:
                cv2.putText(frame, "Failure to detect tracking!!", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            k = cv2.waitKey(1) & 0xff
            if k == 27:
                break

        else:
            break

if __name__ == "__main__":
    selected_tracker = parse()
    print(str(selected_tracker) + " is selected")

    start_tracking(selected_tracker)