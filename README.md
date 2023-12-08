# face-detection-and-capture

This Python script utilizes OpenCV and face_recognition to perform real-time face detection through a camera feed. The script allows users to capture and save images of detected faces along with the person's name.

## Prerequisites

Before running the script, ensure you have the required libraries installed:

```bash
pip install opencv-python face_recognition
```

Run the script:
```bash
python capture.py
```
The script will initialize the camera and display a live feed with rectangles around detected faces.

Capture and Save Images:

Press Enter to capture and save an image of detected faces.
If faces are detected, the script will prompt you to enter the person's name.
Images will be saved in the "images" folder with filenames like "name_1.jpeg", "name_2.jpeg", and so on.
Exit the Application:

Close the script by pressing Enter after capturing the desired images.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify the content, include additional sections, or customize it to better fit your project's specifics.

