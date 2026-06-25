import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

seq = ""
new_nuc = None

def letterbox(frame, target_w, target_h):
    h, w = frame.shape[:2]
    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(frame, (new_w, new_h))
    result = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2
    result[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized
    return result

def letterbox_gray(frame, target_w, target_h):
    h, w = frame.shape[:2]
    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(frame, (new_w, new_h))
    result = np.zeros((target_h, target_w), dtype=np.uint8)
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2
    result[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized
    return result

def read_leds():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    video_file = askopenfilename(parent=root)
    root.destroy()

    global seq

    cv2.namedWindow('Movie', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Movie', 800, 600)
    cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Test', 400, 300)

    while True:
        ret, frame = cap.read()

        if ret:
            display_frame = letterbox(frame, 800, 600)
            cv2.imshow('Movie', display_frame)
            cv2.waitKey(1)
            decode_frame(frame)

        else:
            print("The nuc seq is :" + seq)
            cap.release()
            cv2.destroyAllWindows()
            break


def decode_frame(frame):
    global seq
    global new_nuc

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    print("new nuc: " + str(new_nuc))

    if not any([red_on(frame_hsv), green_on(frame_hsv), blue_on(frame_hsv), yellow_on(frame_hsv)]):
        new_nuc = True
        if all([red_on(frame_hsv), green_on(frame_hsv), blue_on(frame_hsv), yellow_on(frame_hsv)]):
            print("The DNA sequence is : " + seq)
            seq = ""
        else:
            pass
    else:
        if new_nuc:
            print("I'm here")
            if red_on(frame_hsv):
                seq = seq + "A"
                new_nuc = False
            elif green_on(frame_hsv):
                seq = seq + "G"
                new_nuc = False
            elif blue_on(frame_hsv):
                seq = seq + "T"
                new_nuc = False
            elif yellow_on(frame_hsv):
                seq = seq + "C"
                new_nuc = False
            else:
                seq = seq + "N"
                new_nuc = False

            print(seq)

        else:
            pass


def red_on(frame):
    lower_red1 = np.array([0, 200, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 200, 100])
    upper_red2 = np.array([179, 255, 255])

    mask0 = cv2.inRange(frame, lower_red1, upper_red1)
    mask1 = cv2.inRange(frame, lower_red2, upper_red2)

    mask = mask0 + mask1

    return detect_on(frame, mask)


def green_on(frame):
    lower_green = np.array([35, 200, 200])
    upper_green = np.array([75, 255, 255])

    mask = cv2.inRange(frame, lower_green, upper_green)

    return detect_on(frame, mask)


def yellow_on(frame):
    lower_yellow = np.array([25, 200, 200])
    upper_yellow = np.array([35, 255, 255])

    mask = cv2.inRange(frame, lower_yellow, upper_yellow)

    return detect_on(frame, mask)


def blue_on(frame):
    lower_blue = np.array([100, 200, 200])
    upper_blue = np.array([135, 255, 255])

    mask = cv2.inRange(frame, lower_blue, upper_blue)

    return detect_on(frame, mask)


def detect_on(frame, mask):
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)
    masked_frame = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    masked_frame = cv2.threshold(masked_frame, 2, 255, cv2.THRESH_BINARY)[1]
    detected = cv2.countNonZero(masked_frame) > 100

    display_masked = letterbox_gray(masked_frame, 400, 300)
    cv2.imshow('Test', display_masked)
    cv2.waitKey(1)

    return detected


read_leds()