import threading
import cv2
import os
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

ref_images_folder = "ref_imgs"
ref_image_paths = [os.path.join(ref_images_folder, f) for f in os.listdir(ref_images_folder) if f.endswith(('.jpg', '.png'))]
ref_images = []

for path in ref_image_paths:
    try:
        img = cv2.imread(path)
        if img is None:
            raise ValueError(f"Image PATH {path} may be incorrect/Image may be invalid")
        ref_images.append(img)
    except Exception as e:
        print(f"Error loading reference image {path}: {e}")
        exit()

def check_face(frame):
    global face_match
    try:
        for ref_img in ref_images:
            result = DeepFace.verify(frame, ref_img, enforce_detection=False)
            if result['verified']:
                face_match = True
                break
            else:
                face_match = False

    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()

            except ValueError:
                pass
        counter += 1

        if face_match:
            x, y, w, h = 20, 20, 600, 440
            roi = frame[y:y+h, x:x+w]
            blurred_roi = cv2.GaussianBlur(roi, (99, 99), 0)
            frame[y:y+h, x:x+w] = blurred_roi
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q") or key == ord("Q"):
        break

cv2.destroyAllWindows()
