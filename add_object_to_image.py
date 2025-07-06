import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
image[:] = 255, 0, 0

# Add Shapes(Line, Rectangle & Circle) To An Image

cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (0, 255, 0), 3)
cv2.rectangle(image, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(image, (400, 50), 30, (255, 255, 0), 5)

# Add Text To An Image

cv2.putText(image, "Sample Text", (270, 115), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)

cv2.imshow("OpenCV Basics - Add Objects To Image", image)

cv2.waitKey(0)
