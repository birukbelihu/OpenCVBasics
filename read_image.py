import cv2

image = cv2.imread("assets/sample_image.png")

cv2.imshow("OpenCV Basics(Read - Image)", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
