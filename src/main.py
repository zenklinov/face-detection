import cv2
from face_detection import detect_faces

# Start video streaming from webcam
video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    result_frame = detect_faces(frame)
    cv2.imshow('Video', result_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
