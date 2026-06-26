import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

list_seq = []
seq = ""
new_nuc = None

def read_leds():
    Tk().withdraw()
    video_file = askopenfilename()
    cap = cv2.VideoCapture(video_file)

    global seq
    global list_seq

    while True:

        ret, frame = cap.read()

        if ret:
            decode_frame(frame)

        else:
            print("The DNA sequences are : ")
            list_seq.append(seq)
            for seq in list_seq:
                print("- " + seq)
            cap.release()
            cv2.destroyAllWindows()
            break



def decode_frame(frame):
    global seq
    global list_seq
    global new_nuc

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    if not any([red_on(frame_hsv), green_on(frame_hsv), blue_on(frame_hsv), yellow_on(frame_hsv)]):
        new_nuc = True


    if new_nuc:

        if all_on(frame_hsv):
            print("The DNA sequence is : " + seq)
            new_nuc = False
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
    masked_frame = cv2.bitwise_and(frame[200:1000, 200:700], frame[200:1000, 200:700], mask=mask[200:1000, 200:700])
    masked_frame_grey = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    masked_frame_grey = cv2.threshold(masked_frame_grey, 2, 255, cv2.THRESH_BINARY)[1]
    detected = cv2.countNonZero(masked_frame_grey) > px_threshold
    concat_frame_0 = np.concatenate((cv2.cvtColor(frame[200:1000, 200:700],cv2.COLOR_HSV2BGR), masked_frame), axis=1)
    concat_frame_1 = np.concatenate((concat_frame_0, cv2.cvtColor(masked_frame_grey, cv2.COLOR_GRAY2BGR)), axis=1)
    concat_frame_border = cv2.copyMakeBorder(concat_frame_1, 10, 50, 10, 10, cv2.BORDER_CONSTANT, 0)
    cv2.putText(concat_frame_border, "Video Input", (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(concat_frame_border, "Color Mask", (530, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(concat_frame_border, "Grey Mask", (1050, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(concat_frame_border, "Sequence : " + seq, (10,840), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255, 255), 1, cv2.LINE_AA)
    concat_frame_border = cv2.resize(concat_frame_border, (0,0), fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
    cv2.imshow('Decoder', concat_frame_border)
    cv2.waitKey(1)

    return detected



read_leds()


