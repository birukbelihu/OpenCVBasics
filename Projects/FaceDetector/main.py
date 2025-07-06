import cv2

videocapture = cv2.VideoCapture(1)

while videocapture.isOpened():
    isSuccess, image = videocapture.read()
    if isSuccess:
        resized_image = cv2.resize(image, (500, 500))
        grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        face_cascade_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces = face_cascade_classifier.detectMultiScale(grayscale_image, 1.1, 3)

        for (x, y, width, height) in faces:
            cv2.rectangle(resized_image, (x, y), (x + width, y + height), (255, 0, 0), 1)
            cv2.putText(resized_image, "Face", (x, y), cv2.QT_FONT_NORMAL, 0.5, (232, 161, 19), 2)

        cv2.imshow("Face Detector", resized_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

videocapture.release()
cv2.destroyAllWindows()
