import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

list_seq = []
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
    Tk().withdraw()
    video_file = askopenfilename()
    cap = cv2.VideoCapture(video_file)

    global seq
    global list_seq

    cv2.namedWindow('Movie', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Movie', 800, 600)
    cv2.namedWindow('Mask Gray', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mask Gray', 600, 500)
    cv2.namedWindow('Mask Color', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mask Color', 600, 500)

    while True:

        ret, frame = cap.read()

        if ret:
            display_frame = letterbox(frame, 800, 600)
            cv2.imshow('Movie', display_frame)
            cv2.waitKey(1)
            decode_frame(frame)

        else:
            print("The DNA sequences are : ")
            list_seq.append(seq)
            for seq in list_seq:
                print("- " + seq + "\n")
            cap.release()
            cv2.destroyAllWindows()
            break


def decode_frame(frame):
    global seq
    global list_seq
    global new_nuc

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    print("A : " + str(red_on(frame_hsv)) + ", G : " + str(green_on(frame_hsv)) + ", T : " + str(blue_on(frame_hsv)) + " , C : " + str(yellow_on(frame_hsv)))
    print(seq)

    if not any([red_on(frame_hsv), green_on(frame_hsv), blue_on(frame_hsv), yellow_on(frame_hsv)]):
        new_nuc = True

    if new_nuc:

        if all_on(frame_hsv):
            print("The DNA sequence is : " + seq)
            if seq != "":
                list_seq.append(seq)
            else:
                pass

            seq = ""

        elif red_on(frame_hsv):
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
            pass

        print(seq)


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

def all_on(frame):
    lower_all = np.array([0, 0, 250])
    upper_all = np.array([179, 10, 255])
    mask = cv2.inRange(frame, lower_all, upper_all)
    return detect_on(frame, mask, 20000)


def detect_on(frame, mask, px_threshold=2000):
    roi = frame[200:1000, 200:700]
    roi_mask = mask[200:1000, 200:700]

    masked_frame = cv2.bitwise_and(roi, roi, mask=roi_mask)

    # Fenêtre masque couleur (BGR)
    display_color = letterbox(masked_frame, 400, 300)
    cv2.imshow('Mask Color', display_color)

    # Fenêtre masque niveaux de gris
    masked_gray = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    masked_gray = cv2.threshold(masked_gray, 2, 255, cv2.THRESH_BINARY)[1]
    detected = cv2.countNonZero(masked_gray) > px_threshold

    display_masked = letterbox_gray(masked_gray, 400, 300)
    cv2.imshow('Mask Gray', display_masked)
    cv2.waitKey(1)

    return detected


read_leds()