import cv2

HEIGHT, WIDTH = 500, 500

image = cv2.imread("assets/sample_image.png")
resized_image = cv2.resize(image, (HEIGHT, WIDTH))
blur_image = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("OpenCV Basics(Blur Image)", blur_image)

cv2.waitKey(0)
