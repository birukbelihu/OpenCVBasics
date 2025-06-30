import cv2

image = cv2.imread("assets/sample_image.png")
cropped_image = image[100:400, 400:700]

cv2.imshow("OpenCV Basics - Crop Image", cropped_image)

cv2.waitKey(0)
