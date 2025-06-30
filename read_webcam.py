import cv2

videocapture = cv2.VideoCapture(0)

while videocapture.isOpened():
    is_successful, image = videocapture.read()
    if is_successful:
        cv2.imshow("OpenCV Basics - Read Webcam", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

videocapture.release()
