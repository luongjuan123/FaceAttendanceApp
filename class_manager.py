import os
import json
from paths import ensure_data_directory

CLASS_FILE = os.path.join("attendance_data", "classes.json")

def initialize_classes():
    ensure_data_directory()
    if not os.path.exists(CLASS_FILE):
        with open(CLASS_FILE, 'w') as f:
            json.dump([], f)

def get_all_classes():
    try:
        with open(CLASS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def add_class(class_name):
    classes = get_all_classes()
    if class_name and class_name not in classes:
        classes.append(class_name)
        with open(CLASS_FILE, 'w') as f:
            json.dump(sorted(classes), f)
        return True
    return False

def delete_class(class_name):
    classes = get_all_classes()
    if class_name in classes:
        classes.remove(class_name)
        with open(CLASS_FILE, 'w') as f:
            json.dump(classes, f)
        return True
    return False