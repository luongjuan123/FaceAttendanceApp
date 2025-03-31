import os
import json
import cv2
import numpy as np
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QTimer
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
import face_recognition
import datetime
from paths import get_class_attendance_file
from ui_styles import get_capture_stylesheet, get_mark_capture_stylesheet
from class_manager import get_all_classes

class AnimatedButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None, icon_path=None):
        super().__init__(text, parent)
        self.setMouseTracking(True)
        self.animation = None
        self.glow_animation = None
        self.original_geometry = self.geometry()

        if icon_path:
            self.setIcon(QtGui.QIcon(icon_path))
            self.setIconSize(QtCore.QSize(24, 24))

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QtGui.QColor(37, 99, 235, 127))
        self.setGraphicsEffect(self.shadow)

    def enterEvent(self, event):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(self.geometry())
        self.original_geometry = self.geometry()
        new_geometry = QRect(
            self.x() - 5, self.y() - 5,
            self.width() + 10, self.height() + 10
        )
        self.animation.setEndValue(new_geometry)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.animation.start()

        self.glow_animation = QPropertyAnimation(self, b"windowOpacity")
        self.glow_animation.setDuration(500)
        self.glow_animation.setStartValue(1.0)
        self.glow_animation.setEndValue(0.8)
        self.glow_animation.setLoopCount(-1)
        self.glow_animation.setEasingCurve(QEasingCurve.Type.InOutSine)
        self.glow_animation.start()

        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QtGui.QColor(59, 130, 246, 178))
        self.setGraphicsEffect(self.shadow)

        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.original_geometry)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.animation.start()

        if self.glow_animation:
            self.glow_animation.stop()
            self.setWindowOpacity(1.0)

        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtGui.QColor(37, 99, 235, 127))
        self.setGraphicsEffect(self.shadow)

        super().leaveEvent(event)

    def mousePressEvent(self, event):
        shake_animation = QPropertyAnimation(self, b"pos")
        shake_animation.setDuration(50)
        shake_animation.setStartValue(self.pos())
        shake_animation.setKeyValueAt(0.25, self.pos() + QtCore.QPoint(2, 0))
        shake_animation.setKeyValueAt(0.5, self.pos() + QtCore.QPoint(-2, 0))
        shake_animation.setKeyValueAt(0.75, self.pos() + QtCore.QPoint(2, 0))
        shake_animation.setEndValue(self.pos())
        shake_animation.start()

        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtGui.QColor(37, 99, 235, 76))
        self.setGraphicsEffect(self.shadow)

        super().mousePressEvent(event)

class CaptureDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Capture Images")
        self.setFixedSize(700, 650)
        self.current_image_index = 0
        self.captured_images = []
        self.video_capture = cv2.VideoCapture(0)
        self.camera_opened = self.video_capture.isOpened()
        if not self.camera_opened:
            QtWidgets.QMessageBox.critical(self, "Error", "Cannot access camera. Please check your device.")
            self.reject()
            return
        self.initUI()
        self.setStyleSheet(get_capture_stylesheet())

    def initUI(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Camera frame
        camera_frame = QtWidgets.QGroupBox("Camera Preview")
        camera_layout = QtWidgets.QVBoxLayout()
        camera_layout.setSpacing(10)
        camera_frame.setLayout(camera_layout)

        self.status_label = QtWidgets.QLabel(f"Capturing Image {self.current_image_index + 1}")
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 18px; color: #7aa2f7;")
        camera_layout.addWidget(self.status_label)

        self.image_label = QtWidgets.QLabel()
        self.image_label.setFixedSize(640, 480)
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background: #24283b; border: 2px solid #414868; border-radius: 12px;")
        camera_layout.addWidget(self.image_label)

        main_layout.addWidget(camera_frame)

        # Buttons
        self.button_layout = QtWidgets.QGridLayout()
        self.button_layout.setSpacing(10)

        self.capture_button = AnimatedButton("Capture", icon_path="camera_icon.png")
        self.capture_button.clicked.connect(self.capture_image)
        self.button_layout.addWidget(self.capture_button, 0, 0)

        self.retake_button = AnimatedButton("Retake", icon_path="retake_icon.png")
        self.retake_button.clicked.connect(self.retake_image)
        self.retake_button.setVisible(False)
        self.button_layout.addWidget(self.retake_button, 0, 1)

        self.confirm_button = AnimatedButton("Confirm", icon_path="confirm_icon.png")
        self.confirm_button.clicked.connect(self.confirm_image)
        self.confirm_button.setVisible(False)
        self.button_layout.addWidget(self.confirm_button, 0, 2)

        self.button_layout.setColumnStretch(0, 1)
        self.button_layout.setColumnStretch(1, 1)
        self.button_layout.setColumnStretch(2, 1)
        main_layout.addLayout(self.button_layout)
        self.setLayout(main_layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        if self.camera_opened:
            ret, frame = self.video_capture.read()
            if not ret:
                frame = np.zeros((480, 640, 3), dtype=np.uint8)
        else:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        bytes_per_line = ch * w
        image = QtGui.QImage(frame_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))

    def capture_image(self):
        if not self.camera_opened:
            QtWidgets.QMessageBox.warning(self, "Error", "Camera not available.")
            return

        ret, frame = self.video_capture.read()
        if ret:
            temp_path = f"temp_image_{self.current_image_index}.jpg"
            cv2.imwrite(temp_path, frame)
            self.captured_images.append(temp_path)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            image = QtGui.QImage(frame_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))

            self.status_label.setText(f"Confirm Image {self.current_image_index + 1}")
            self.capture_button.setVisible(False)
            self.retake_button.setVisible(True)
            self.confirm_button.setVisible(True)
            self.button_layout.removeWidget(self.capture_button)
            self.button_layout.addWidget(self.retake_button, 0, 0)
            self.button_layout.addWidget(self.confirm_button, 0, 1)
            self.button_layout.removeWidget(self.retake_button)
            self.button_layout.removeWidget(self.confirm_button)

            self.timer.stop()

    def retake_image(self):
        if self.captured_images:
            os.remove(self.captured_images.pop())

        self.status_label.setText(f"Capturing Image {self.current_image_index + 1}")
        self.retake_button.setVisible(False)
        self.confirm_button.setVisible(False)
        self.button_layout.removeWidget(self.retake_button)
        self.button_layout.removeWidget(self.confirm_button)
        self.capture_button.setVisible(True)
        self.button_layout.addWidget(self.capture_button, 0, 0)
        self.button_layout.removeWidget(self.capture_button)

        self.timer.start(30)

    def confirm_image(self):
        self.current_image_index += 1
        if self.current_image_index < 3:
            self.status_label.setText(f"Capturing Image {self.current_image_index + 1}")
            self.retake_button.setVisible(False)
            self.confirm_button.setVisible(False)
            self.button_layout.removeWidget(self.retake_button)
            self.button_layout.removeWidget(self.confirm_button)
            self.capture_button.setVisible(True)
            self.button_layout.addWidget(self.capture_button, 0, 0)
            self.button_layout.removeWidget(self.capture_button)
            self.timer.start(30)
        else:
            self.accept()

    def closeEvent(self, event):
        self.timer.stop()
        self.video_capture.release()
        event.accept()

    def get_captured_images(self):
        return self.captured_images

class MarkCaptureDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("mark_attendance_dialog")
        self.setWindowTitle("Mark Attendance")
        self.setFixedSize(700, 650)
        self.parent = parent
        self.video_capture = cv2.VideoCapture(0)
        self.camera_opened = self.video_capture.isOpened()
        if not self.camera_opened:
            QtWidgets.QMessageBox.critical(self, "Error", "Cannot access camera. Please check your device.")
            self.reject()
            return
        self.recognized_ids = set()
        self.is_recognizing = False
        self.initUI()
        self.image_label.setObjectName("camera_label")
        self.status_label.setObjectName("status_label")
        self.setStyleSheet(get_mark_capture_stylesheet())

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        self.status_label = QtWidgets.QLabel("Press Start to begin recognition")
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.shortcut_label = QtWidgets.QLabel("Press Space to start recognition or use Start button")
        self.shortcut_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.shortcut_label.setStyleSheet("font-size: 12px; color: #D1D5DB;")
        layout.addWidget(self.shortcut_label)

        self.image_label = QtWidgets.QLabel()
        self.image_label.setFixedSize(640, 480)
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.button_layout = QtWidgets.QGridLayout()
        self.button_layout.setSpacing(10)

        self.start_button = AnimatedButton("Start", icon_path="start_icon.png")
        self.start_button.clicked.connect(self.start_recognition)
        self.button_layout.addWidget(self.start_button, 0, 0)

        self.mark_button = AnimatedButton("Mark", icon_path="mark_icon.png")
        self.mark_button.clicked.connect(self.mark_attendance)
        self.mark_button.setVisible(False)
        self.button_layout.addWidget(self.mark_button, 0, 1)

        self.confirm_button = AnimatedButton("Confirm", icon_path="confirm_icon.png")
        self.confirm_button.clicked.connect(self.confirm_recognition)
        self.confirm_button.setVisible(False)
        self.button_layout.addWidget(self.confirm_button, 0, 2)

        self.button_layout.setColumnStretch(0, 1)
        self.button_layout.setColumnStretch(1, 1)
        self.button_layout.setColumnStretch(2, 1)

        layout.addLayout(self.button_layout)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        if self.camera_opened:
            ret, frame = self.video_capture.read()
            if not ret:
                frame = np.zeros((480, 640, 3), dtype=np.uint8)
        else:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if self.is_recognizing:
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.parent.known_face_encodings, face_encoding)
                if True in matches:
                    first_match_index = matches.index(True)
                    student_id = self.parent.known_face_ids[first_match_index]
                    self.recognized_ids.add(student_id)

                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, student_id, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                              0.9, (0, 255, 0), 2, cv2.LINE_AA)

            if self.recognized_ids:
                self.status_label.setText(f"Recognized: {', '.join(self.recognized_ids)}")
            else:
                self.status_label.setText("Recognizing... No faces detected yet.")

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        bytes_per_line = ch * w
        image = QtGui.QImage(frame_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))

    def start_recognition(self):
        if not hasattr(self.parent, 'known_face_encodings') or not self.parent.known_face_encodings:
            self.status_label.setText("No known faces to recognize.")
            return

        if not self.camera_opened:
            self.status_label.setText("Camera not available.")
            return

        self.is_recognizing = True
        self.start_button.setVisible(False)
        self.mark_button.setVisible(True)
        self.confirm_button.setVisible(True)
        self.shortcut_label.setText("Press Space to mark attendance or use Mark button")
        self.status_label.setText("Recognizing...")

        self.button_layout.removeWidget(self.start_button)
        self.button_layout.addWidget(self.mark_button, 0, 0)
        self.button_layout.addWidget(self.confirm_button, 0, 1)
        self.button_layout.removeWidget(self.mark_button)
        self.button_layout.removeWidget(self.confirm_button)

    def mark_attendance(self):
        if self.recognized_ids:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            attendance_file = get_class_attendance_file(self.parent.current_class)
            try:
                with open(attendance_file, 'r') as f:
                    data = json.load(f)
            except:
                data = {}

            for student_id in self.recognized_ids:
                if student_id not in data:
                    data[student_id] = {
                        "name": self.parent.known_face_names[self.parent.known_face_ids.index(student_id)],
                        "attendance": {}
                    }
                data[student_id]["attendance"][today] = True

            with open(attendance_file, 'w') as f:
                json.dump(data, f, indent=4)

            self.status_label.setText(f"Marked attendance for: {', '.join(self.recognized_ids)}")
        else:
            self.status_label.setText("No faces recognized to mark.")

    def confirm_recognition(self):
        self.is_recognizing = False
        self.start_button.setVisible(True)
        self.mark_button.setVisible(False)
        self.confirm_button.setVisible(False)
        self.shortcut_label.setText("Press Space to start recognition or use Start button")
        self.status_label.setText("Recognition stopped.")

        self.button_layout.removeWidget(self.mark_button)
        self.button_layout.removeWidget(self.confirm_button)
        self.button_layout.addWidget(self.start_button, 0, 0)
        self.button_layout.removeWidget(self.start_button)
        self.accept()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Space:
            if not self.is_recognizing:
                self.start_recognition()
            else:
                self.mark_attendance()
        super().keyPressEvent(event)

    def closeEvent(self, event):
        self.timer.stop()
        self.video_capture.release()
        event.accept()

    def get_recognized_ids(self):
        return self.recognized_ids

class LoginDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(400, 400)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        self.email_input = QtWidgets.QLineEdit()
        self.email_input.setPlaceholderText("Email ID")
        layout.addWidget(self.email_input)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        hbox = QtWidgets.QHBoxLayout()
        self.remember_checkbox = QtWidgets.QCheckBox("Remember me")
        hbox.addWidget(self.remember_checkbox)

        forgot_label = QtWidgets.QLabel("<a href='#'>Forgot Password?</a>")
        forgot_label.setStyleSheet("color: #6B7280; text-decoration: underline;")
        forgot_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        hbox.addWidget(forgot_label)

        layout.addLayout(hbox)

        login_button = AnimatedButton("LOGIN")
        login_button.clicked.connect(self.accept)
        login_button.setFixedHeight(50)
        layout.addWidget(login_button)

        self.setLayout(layout)

class AddStudentDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Student")
        self.setFixedSize(400, 500)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        self.class_combo = QtWidgets.QComboBox()
        self.class_combo.addItems(get_all_classes())
        self.class_combo.setView(QtWidgets.QListView())
        self.class_combo.setMaxVisibleItems(10)
        layout.addWidget(QtWidgets.QLabel("Class:"))
        layout.addWidget(self.class_combo)

        self.student_id_input = QtWidgets.QLineEdit()
        self.student_id_input.setPlaceholderText("Student ID")
        layout.addWidget(QtWidgets.QLabel("Student ID:"))
        layout.addWidget(self.student_id_input)

        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setPlaceholderText("Name")
        layout.addWidget(QtWidgets.QLabel("Name:"))
        layout.addWidget(self.name_input)

        self.capture_button = AnimatedButton("Capture Images (3 required)", icon_path="camera_icon.png")
        self.capture_button.clicked.connect(self.capture_images)
        layout.addWidget(self.capture_button)

        self.image_paths = []
        self.image_labels = []
        for i in range(3):
            label = QtWidgets.QLabel(f"Image {i + 1}: Waiting...")
            self.image_labels.append(label)
            layout.addWidget(label)

        self.add_button = AnimatedButton("Add Student", icon_path="add_icon.png")
        self.add_button.clicked.connect(self.validate_and_accept)
        self.add_button.setEnabled(False)
        layout.addWidget(self.add_button)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

        self.class_combo.setStyleSheet("""
            QComboBox {
                background: #2563EB;
                border: none;
                border-radius: 15px;
                padding: 12px 24px;
                color: #FFFFFF;
                font-weight: bold;
                font-size: 14px;
                min-width: 120px;
            }
            QComboBox:hover {
                background-color: #3B82F6;
            }
            QComboBox::drop-down {
                width: 30px;
                border: none;
                background: transparent;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 16px;
                height: 16px;
                margin-right: 8px;
            }
            QComboBox QAbstractItemView {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4B5EAA, stop:1 #2E3B5E);
                border: none;
                border-radius: 15px;
                color: white;
                selection-background-color: #2563EB;
                padding: 5px;
                margin: 0px;
            }
            QComboBox QAbstractItemView::item {
                height: 30px;
                padding: 5px;
                border: none;
                border-radius: 10px;
            }
        """)

    def capture_images(self):
        capture_dialog = CaptureDialog(self)
        if capture_dialog.exec():
            self.image_paths = capture_dialog.get_captured_images()
            for i in range(len(self.image_paths)):
                self.image_labels[i].setText(f"Image {i + 1}: Captured")
            if len(self.image_paths) == 3:
                self.add_button.setEnabled(True)

    def validate_and_accept(self):
        if len(self.image_paths) != 3:
            QtWidgets.QMessageBox.warning(self, "Error", "Please capture exactly 3 images.")
            return

        if not self.student_id_input.text() or not self.name_input.text():
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        from paths import get_class_folder
        _, faces_dir = get_class_folder(self.class_combo.currentText())
        os.makedirs(faces_dir, exist_ok=True)

        import shutil
        for i, image_path in enumerate(self.image_paths):
            dest_path = os.path.join(faces_dir, f"{self.student_id_input.text()}_{self.name_input.text()}_{i}.jpg")
            shutil.copy(image_path, dest_path)
            if "temp_image" in image_path and os.path.exists(image_path):
                os.remove(image_path)

        self.accept()

class MarkAttendanceDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mark Attendance")
        self.setFixedSize(400, 300)
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        self.camera_button = AnimatedButton("Start Camera", icon_path="camera_icon.png")
        self.camera_button.clicked.connect(self.start_camera)
        layout.addWidget(self.camera_button)

        self.result_label = QtWidgets.QLabel("Attendance not marked yet.")
        layout.addWidget(self.result_label)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Close)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def start_camera(self):
        mark_capture_dialog = MarkCaptureDialog(self.parent())
        if mark_capture_dialog.exec():
            recognized_ids = mark_capture_dialog.get_recognized_ids()
            if recognized_ids:
                self.result_label.setText(f"Marked attendance for: {', '.join(recognized_ids)}")
            else:
                self.result_label.setText("No faces recognized.")