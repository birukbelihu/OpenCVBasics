import cv2

image = cv2.imread("assets/sample_image.png")
resized_image = cv2.resize(image, (500, 500))
canny_image = cv2.Canny(resized_image, 150, 200)

cv2.imshow("OpenCV Basics", canny_image)

cv2.waitKey(0)
