import cv2

height, width = 500, 500

image = cv2.imread("assets/sample_image.png")
resized_image = cv2.resize(image, (height, width))
grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

cv2.imshow("OpenCV Basics - Grayscale Image", grayscale_image)

cv2.waitKey(0)
