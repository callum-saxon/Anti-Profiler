# Profiler

This simple Python script utilizes the OpenCV and DeepFace libraries to perform real-time face recognition using a webcam. The script captures video frames, compares them with a reference image, and displays whether a match is found or not.

## Dependencies

Make sure you have the following dependencies installed:

- OpenCV
- DeepFace

Install them using:

```bash
pip install opencv-python deepface
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/callum-saxon/Anti-Profiler.git
```

2. Navigate to the project directory:

```bash
cd Anti-Profiler
```

3. Place your reference image as "ref.jpg" in the project directory.

4. Run the script:

```bash
python main.py
```

Press 'q' to exit the application.

## To Note

- Adjust the webcam index (`cv2.VideoCapture(0)`) if you have multiple cameras.
- Ensure that the reference image ("ref.jpg") contains a clear and recognizable face for accurate matching.

Feel free to customize and integrate this code into your projects. Happy coding!
