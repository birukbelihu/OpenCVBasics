import cv2
import numpy as np

width = 250
height = 350

image = cv2.imread("assets/sample_image_3.jpg")

face_cascade_classifier = cv2.CascadeClassifier("assets/haarcascades/haarcascade_frontalface_default.xml")

initial_points = np.float32([[176, 152], [485, 123], [211, 638], [530, 612]])
final_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(initial_points, final_points)
img = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("OpenCV Warp Perspective", img)

cv2.waitKey(0)
