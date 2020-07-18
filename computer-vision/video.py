import cv2
import numpy as np


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

while True:
    signal, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv_lower = np.array([90, 100, 100])
    hsv_upper = np.array([130, 255, 255])

    mask = cv2.inRange(hsv_frame, hsv_lower, hsv_upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Camera frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("object", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
