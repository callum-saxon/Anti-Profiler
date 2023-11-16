import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
ref_img = cv2.imread("ref.jpg")

try:
    ref_img = cv2.imread("ref.jpg")
    if ref_img is None:
        raise ValueError("Image PATH may be inccorrect/Image may be invalid")
except Exception as e:
    print(f"Error loading reference image: {e}")
    exit()

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, ref_img, enforce_detection=False)
        if result['verified']:
            face_match = True
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
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q") or key == ord("Q"):
        break

cv2.destroyAllWindows()
