import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

def nothing(x):
    pass


cv2.namedWindow('Tracking')

cv2.createTrackbar('LH', "Tracking", 0, 255, nothing)
cv2.createTrackbar('LS', "Tracking", 0, 255, nothing)
cv2.createTrackbar('LV', "Tracking", 0, 255, nothing)

cv2.createTrackbar('HH', "Tracking", 0, 255, nothing)
cv2.createTrackbar('HS', "Tracking", 0, 255, nothing)
cv2.createTrackbar('HV', "Tracking", 0, 255, nothing)

while True:
    b, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', "Tracking")
    l_s = cv2.getTrackbarPos('LS', "Tracking")
    l_v = cv2.getTrackbarPos('LV', "Tracking")

    h_h = cv2.getTrackbarPos('HH', "Tracking")
    h_s = cv2.getTrackbarPos('HS', "Tracking")
    h_v = cv2.getTrackbarPos('HV', "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([h_h, h_s, h_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)  # isolates the object based on the color
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()









