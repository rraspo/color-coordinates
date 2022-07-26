# Python program for Detection of a
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np


def doNothing(x): pass


cv2.namedWindow('trackbar')

# Webcam no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

cv2.createTrackbar('Hue Lower', 'trackbar', 0, 255, doNothing)
cv2.createTrackbar('Saturation Lower', 'trackbar', 0, 255, doNothing)
cv2.createTrackbar('Value Lower', 'trackbar', 0, 255, doNothing)

cv2.createTrackbar('Hue Higher', 'trackbar', 255, 255, doNothing)
cv2.createTrackbar('Saturation Higher', 'trackbar', 255, 255, doNothing)
cv2.createTrackbar('Value Higher', 'trackbar', 255, 255, doNothing)

# This drives the program into an infinite loop.
while True:
    # Capture the live stream frame-by-frame
    _, frame = cap.read()
    # Convert images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower_blue = np.array([50, 50, 50])
    # upper_blue = np.array([255, 255, 255])
    lower_red = np.array([0, 0, 186])
    upper_red = np.array([101, 168, 255])
    # lower_green = np.array([121, 100, 100])
    # upper_green = np.array([180, 100, 100])

    # blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    # green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res

    # mask = cv2.bitwise_or(blue_mask, green_mask, red_mask)
    # res = cv2.bitwise_and(frame, frame, mask=mask)

    # l_h = cv2.getTrackbarPos('Hue Lower', 'trackbar')
    # l_s = cv2.getTrackbarPos('Saturation Lower', 'trackbar')
    # l_v = cv2.getTrackbarPos('Value Lower', 'trackbar')
    #
    # h_h = cv2.getTrackbarPos('Hue Higher', 'trackbar')
    # h_s = cv2.getTrackbarPos('Saturation Higher', 'trackbar')
    # h_v = cv2.getTrackbarPos('Value Higher', 'trackbar')
    # l_bound = np.array([l_h, l_s, l_v])
    # u_bound = np.array([h_h, h_s, h_v])
    # mask = cv2.inRange(frame, l_bound, u_bound)

    res = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', red_mask)
    cv2.imshow('res', res)
    cv2.imshow('test', hsv)

    # 

    # This displays the frame, mask
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Destroys all the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()
