import cv2

# Load classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    return image

# Function to resize the image to a specific width while maintaining the aspect ratio
def resize_image(image, width):
    # Get the dimensions of the image
    (h, w) = image.shape[:2]
    # Calculate the ratio of the width and construct the new dimensions
    r = width / float(w)
    dim = (width, int(h * r))
    # Resize the image
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

# Load an image from file
image_path = path\to\image.jpg'  # Change this to the path of your image file jpg/png
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print("Error loading image")
else:
    # Detect faces in the image
    result_image = detect_faces(image)
    
    # Resize the result image to a width of 756 pixels
    resized_image = resize_image(result_image, 756)
    
    # Display the result
    cv2.imshow('Image', resized_image)
    
    # Wait until a key is pressed to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
