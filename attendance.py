import os
import json
from datetime import datetime
import face_recognition
from paths import get_class_folder, get_class_attendance_file

def initialize_attendance(class_name):
    attendance_file = get_class_attendance_file(class_name)
    if not os.path.exists(attendance_file):
        with open(attendance_file, 'w') as f:
            json.dump({}, f)

def mark_attendance(student_id, student_name, class_name):
    today = datetime.now().strftime("%Y-%m-%d")
    attendance_file = get_class_attendance_file(class_name)

    try:
        with open(attendance_file, 'r') as f:
            data = json.load(f)
    except:
        data = {}

    if student_id not in data:
        data[student_id] = {
            "name": student_name,
            "class": class_name,
            "attendance": {}
        }

    data[student_id]["attendance"][today] = True

    with open(attendance_file, 'w') as f:
        json.dump(data, f, indent=4)

    return True

def load_known_faces(class_name):
    _, faces_dir = get_class_folder(class_name)
    known_face_encodings = []
    known_face_ids = []
    known_face_names = []

    for filename in os.listdir(faces_dir):
        if filename.endswith(".jpg"):
            parts = filename.split('_')
            student_id = parts[0]
            student_name = parts[1]

            image_path = os.path.join(faces_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)

            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_ids.append(student_id)
                known_face_names.append(student_name)

    return known_face_encodings, known_face_ids, known_face_names