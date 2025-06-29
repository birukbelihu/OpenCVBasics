import cv2

videocapture = cv2.VideoCapture(0)

while videocapture.isOpened():
    isSuccess, image = videocapture.read()
    if isSuccess:
        cv2.imshow("OpenCV Basics(Read Webcam)", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

videocapture.release()
