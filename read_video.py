import cv2

video_capture = cv2.VideoCapture("assets/sample_video.mp4")

while video_capture.isOpened():
    is_successful, image = video_capture.read()
    if is_successful:
        cv2.imshow("OpenCV Basics", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

video_capture.release()
