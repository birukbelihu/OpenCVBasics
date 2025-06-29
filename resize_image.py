import cv2

image = cv2.imread("assets/sample_image.png")
resized_image = cv2.resize(image, (500, 500))

cv2.imshow("OpenCV Basics", resized_image)

cv2.waitKey(0)
