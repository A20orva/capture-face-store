import cv2
import face_recognition
import os

# Create the "images" folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Get the current number of images in the folder
existing_images = [f for f in os.listdir("images") if f.endswith('.jpg')]
counter = len(existing_images) + 1

# Initialize the camera
cap = cv2.VideoCapture(0)

# Display a message to the user
print("Press Enter to capture and save an image.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)

    # Draw rectangles around the faces with additional space
    for (top, right, bottom, left) in face_locations:
        # Define the additional space around the face
        padding = 100
        top = max(0, top - padding)
        right = min(frame.shape[1], right + padding)
        bottom = min(frame.shape[0], bottom + padding)
        left = max(0, left - padding)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Wait for the user to press Enter
    key = cv2.waitKey(1)
    if key == 13:  # Enter key
        # If faces are detected, capture and save the images
        if len(face_locations) > 0:
            print(f"Number of faces detected: {len(face_locations)}")

            # Take user input for the person's name
            name = input("Enter the person's name: ")

            # Capture and save images for all detected faces
            for i, (top, right, bottom, left) in enumerate(face_locations):
                # Define the additional space around the face
                padding = 100
                top = max(0, top - padding)
                right = min(frame.shape[1], right + padding)
                bottom = min(frame.shape[0], bottom + padding)
                left = max(0, left - padding)

                face_img = frame[top:bottom, left:right]
                img_name = f"images/{name}.jpeg"
                cv2.imwrite(img_name, face_img)
                print(f"Image captured and saved as {img_name}")

            counter += 1

        # Break out of the loop after saving images
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
