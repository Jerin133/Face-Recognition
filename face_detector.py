import cv2
import os
import csv
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def recognize_face():
    import threading

    # Load student data from CSV
    students = {}
    try:
        with open('jerin.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students[row['Roll No']] = {
                    'name': row['Name'],
                    'department': row['Department'],
                    'course': row['Course']
                }
    except FileNotFoundError:
        messagebox.showerror("Error", "Student database not found!")
        return

    # Initialize face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Prepare training data
    faces = []
    labels = []
    labels_dict = {}
    current_id = 0

    photos_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'photos')
    if not os.path.exists(photos_dir):
        messagebox.showerror("Error", "Photos directory not found!")
        return

    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    if not os.path.exists(face_cascade_path):
        messagebox.showerror("Error", "Haar cascade file missing!")
        return

    for root, _, files in os.walk(photos_dir):
        for file in files:
            if file.lower().endswith(('jpg', 'png')):
                path = os.path.join(root, file)
                try:
                    roll_no = os.path.splitext(file)[0].split('_')[0]
                    label = roll_no

                    if label not in labels_dict:
                        labels_dict[label] = current_id
                        current_id += 1

                    img = Image.open(path).convert('L')
                    img_np = np.array(img, 'uint8')

                    detected_faces = face_cascade.detectMultiScale(
                        img_np,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(30, 30)
                    )

                    for (x, y, w, h) in detected_faces:
                        faces.append(img_np[y:y+h, x:x+w])
                        labels.append(labels_dict[label])

                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")

    if len(faces) == 0:
        messagebox.showerror("Error", "No faces found in the training images!")
        return

    # Train the recognizer
    recognizer.train(faces, np.array(labels))

    # Use a mutable flag so the thread can be stopped cleanly
    stop_flag = [False]

    def camera_loop():
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        cv2.namedWindow('Face Recognition')

        while not stop_flag[0]:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected_faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            for (x, y, w, h) in detected_faces:
                roi_gray = gray[y:y+h, x:x+w]
                label_id, confidence = recognizer.predict(roi_gray)

                label = None
                for roll_no, lid in labels_dict.items():
                    if lid == label_id:
                        label = roll_no
                        break

                if label and confidence < 70:
                    student = students.get(label, {})
                    name = student.get('name', 'Unknown')
                    dept = student.get('department', 'Unknown')
                    cv2.putText(frame, f"Roll: {label} | {name}", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Unknown", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('Face Recognition', frame)

            key = cv2.waitKey(1) & 0xFF
            # Stop on ESC key OR if the OpenCV window is closed
            if key == 27:
                break
            if cv2.getWindowProperty('Face Recognition', cv2.WND_PROP_VISIBLE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    # Run camera in a daemon thread so it doesn't block Tkinter
    t = threading.Thread(target=camera_loop, daemon=True)
    t.start()

if __name__ == "__main__":
    recognize_face()
