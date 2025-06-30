import cv2

image = cv2.imread("assets/sample.jpg")
resized_image = cv2.resize(image, (500, 500))
grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

face_cascade_classifier = cv2.CascadeClassifier("assets/haarcascades/haarcascade_frontalface_default.xml")
faces = face_cascade_classifier.detectMultiScale(grayscale_image, 1.1, 2)

for (x, y, width, height) in faces:
    cv2.rectangle(resized_image, (x, y), (x + width, y + height), (255, 0, 0), 1)

cv2.imshow("OpenCV Basics - Face Detection", resized_image)

faces_count = len(faces)

if faces_count == 1:
    print(f"{faces_count} Face")
elif faces_count > 1:
    print(f"{faces_count} Faces")

cv2.waitKey(0)

cv2.destroyAllWindows()
