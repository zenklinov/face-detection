import cv2

# Load classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect face in frame
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    return frame

# Start video streaming from webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Take frame from video
    _, frame = video_capture.read()
    
    # Detect face in frame
    result_frame = detect_faces(frame)
    
    # Show result
    cv2.imshow('Video', result_frame)
    
    # Quit from loop if press button 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close video streaming
video_capture.release()
cv2.destroyAllWindows()
