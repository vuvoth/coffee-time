import cv2

img = cv2.imread("./images/me.jpg")

cv2.imshow("hello", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.waitKey(1)
