import os

def ensure_data_directory():
    """Ensure the main data directory exists"""
    os.makedirs("attendance_data", exist_ok=True)

def get_class_folder(class_name):
    """Get paths for a class folder and its faces subfolder"""
    class_dir = os.path.join("attendance_data", f"class_{class_name}")
    faces_dir = os.path.join(class_dir, "faces")
    os.makedirs(faces_dir, exist_ok=True)
    return class_dir, faces_dir

def get_class_attendance_file(class_name):
    """Get path to attendance.json for a class"""
    class_dir, _ = get_class_folder(class_name)
    return os.path.join(class_dir, "attendance.json")