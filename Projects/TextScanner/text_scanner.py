import cv2
import pytesseract

image = cv2.imread("../../assets/sample_image_5.png")
resized_image = cv2.resize(image, (600, 600))

text = pytesseract.image_to_string(resized_image, "amh")

cv2.imshow("OpenCV Text Scanner", resized_image)
print(text)

cv2.waitKey(0)

cv2.destroyAllWindows()
