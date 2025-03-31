import os
import json
import datetime
from PyQt6 import QtWidgets, QtGui, QtCore
from class_manager import initialize_classes, get_all_classes, add_class, delete_class
from attendance import load_known_faces, initialize_attendance
from dialogs import LoginDialog, AddStudentDialog, MarkAttendanceDialog, AnimatedButton
from paths import get_class_folder, get_class_attendance_file
from ui_styles import get_main_stylesheet, get_login_stylesheet, get_add_student_stylesheet, get_mark_attendance_stylesheet

TRANSLATIONS = {
    "en": {
        "app_title": "Face Attendance System",
        "controls": "Controls",
        "class_management": "Class Management",
        "add_new_class": "Add New Class",
        "delete_current_class": "Delete Current Class",
        "student_management": "Student Management",
        "add_new_student": "Add New Student",
        "delete_student": "Delete Student",
        "search_student": "Search Student",
        "attendance": "Attendance",
        "mark_attendance": "Mark Attendance",
        "view_attendance": "View Attendance",
        "attendance_records": "Attendance Records",
        "add_class_title": "Add New Class",
        "enter_class_name": "Enter class name:",
        "add": "Add",
        "cancel": "Cancel",
        "error": "Error",
        "class_exists": "Class already exists or invalid name",
        "confirm_delete": "Confirm Delete",
        "delete_class_confirm": "Delete class {class_name}? This will delete all student data in this class.",
        "select_class_first": "Please select a class first",
        "no_students_to_delete": "No students to delete",
        "delete_student_title": "Delete Student",
        "select_student_to_delete": "Select a student to delete:",
        "confirm_deletion": "Confirm Deletion",
        "delete_student_confirm": "Are you sure you want to delete {name} ({student_id})? This will remove all their data.",
        "student_id": "Student ID",
        "name": "Name",
        "language": "Language",
        "yes": "Yes",
        "no": "No",
        "search": "Search",
        "student_number": "Number",
        "no_results": "No results found",
        "delete": "Delete",
        "student_name": "Name",
        "search_and_delete": "Search and Delete",
        "delete_action": "Action",
    },
    "vi": {
        "app_title": "Hệ thống Điểm danh bằng Khuôn mặt",
        "controls": "Điều khiển",
        "class_management": "Quản lý lớp học",
        "add_new_class": "Thêm lớp mới",
        "delete_current_class": "Xóa lớp hiện tại",
        "student_management": "Quản lý học sinh",
        "add_new_student": "Thêm học sinh mới",
        "delete_student": "Xóa học sinh",
        "search_student": "Tìm kiếm học sinh",
        "attendance": "Điểm danh",
        "mark_attendance": "Đánh dấu điểm danh",
        "view_attendance": "Xem điểm danh",
        "attendance_records": "Hồ sơ điểm danh",
        "add_class_title": "Thêm lớp mới",
        "enter_class_name": "Nhập tên lớp:",
        "add": "Thêm",
        "cancel": "Hủy",
        "error": "Lỗi",
        "class_exists": "Lớp đã tồn tại hoặc tên không hợp lệ",
        "confirm_delete": "Xác nhận xóa",
        "delete_class_confirm": "Xóa lớp {class_name}? Điều này sẽ xóa toàn bộ dữ liệu học sinh trong lớp này.",
        "select_class_first": "Vui lòng chọn lớp trước",
        "no_students_to_delete": "Không có học sinh nào để xóa",
        "delete_student_title": "Xóa học sinh",
        "select_student_to_delete": "Chọn học sinh để xóa:",
        "confirm_deletion": "Xác nhận xóa",
        "delete_student_confirm": "Bạn có chắc chắn muốn xóa {name} ({student_id})? Điều này sẽ xóa toàn bộ dữ liệu của họ.",
        "student_id": "Mã học sinh",
        "name": "Tên",
        "language": "Ngôn ngữ",
        "yes": "Có",
        "no": "Không",
        "search": "Tìm kiếm",
        "student_number": "Số báo danh",
        "no_results": "Không tìm thấy kết quả",
        "delete": "Xóa",
        "student_name": "Tên",
        "search_and_delete": "Tìm kiếm và Xóa",
        "delete_action": "Thao tác",
    },
    "jp": {
        "app_title": "顔認識による出欠システム",
        "controls": "コントロール",
        "class_management": "クラス管理",
        "add_new_class": "新しいクラスを追加",
        "delete_current_class": "現在のクラスを削除",
        "student_management": "生徒管理",
        "add_new_student": "新しい生徒を追加",
        "delete_student": "生徒を削除",
        "search_student": "生徒を検索",
        "attendance": "出欠",
        "mark_attendance": "出欠をマーク",
        "view_attendance": "出欠を表示",
        "attendance_records": "出欠記録",
        "add_class_title": "新しいクラスを追加",
        "enter_class_name": "クラス名を入力:",
        "add": "追加",
        "cancel": "キャンセル",
        "error": "エラー",
        "class_exists": "クラスが既に存在するか、無効な名前です",
        "confirm_delete": "削除の確認",
        "delete_class_confirm": "クラス {class_name} を削除しますか？これにより、このクラスのすべての生徒データが削除されます。",
        "select_class_first": "まずクラスを選択してください",
        "no_students_to_delete": "削除する生徒がいません",
        "delete_student_title": "生徒を削除",
        "select_student_to_delete": "削除する生徒を選択:",
        "confirm_deletion": "削除の確認",
        "delete_student_confirm": "{name} ({student_id}) を削除してもよろしいですか？これにより、彼らのすべてのデータが削除されます。",
        "student_id": "生徒ID",
        "name": "名前",
        "language": "言語",
        "yes": "はい",
        "no": "いいえ",
        "search": "検索",
        "student_number": "番号",
        "no_results": "結果が見つかりません",
        "delete": "削除",
        "student_name": "名前",
        "search_and_delete": "検索と削除",
        "delete_action": "操作",
    }
}

class FaceAttendanceApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        initialize_classes()
        self.current_class = None
        self.user_role = "admin"
        self.current_language = "en"
        self.setWindowTitle(TRANSLATIONS[self.current_language]["app_title"])
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()
        self.setStyleSheet("""
            QWidget {
                font-weight: bold;
            }
            QGroupBox {
                font-size: 16px;
            }
            QGroupBox::title {
                font-size: 18px;
            }
        """)

    def initUI(self):
        main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(main_layout)

        # Control frame
        self.control_frame = QtWidgets.QGroupBox(TRANSLATIONS[self.current_language]["controls"])
        control_layout = QtWidgets.QVBoxLayout()
        self.control_frame.setLayout(control_layout)

        # Class management
        self.class_management_group = QtWidgets.QGroupBox(TRANSLATIONS[self.current_language]["class_management"])
        class_management_layout = QtWidgets.QVBoxLayout()

        self.class_combo = QtWidgets.QComboBox()
        self.class_combo.addItems(get_all_classes())
        self.class_combo.currentTextChanged.connect(self.change_class)
        self.class_combo.setView(QtWidgets.QListView())
        self.class_combo.setMaxVisibleItems(10)
        class_management_layout.addWidget(self.class_combo)

        self.add_class_button = AnimatedButton(TRANSLATIONS[self.current_language]["add_new_class"],
                                               icon_path="add_icon.png")
        self.add_class_button.clicked.connect(self.add_class)
        class_management_layout.addWidget(self.add_class_button)

        self.delete_class_button = AnimatedButton(TRANSLATIONS[self.current_language]["delete_current_class"],
                                                  icon_path="delete_icon.png")
        self.delete_class_button.clicked.connect(self.delete_class)
        class_management_layout.addWidget(self.delete_class_button)

        class_management_layout.addStretch()

        language_label = QtWidgets.QLabel(TRANSLATIONS[self.current_language]["language"])
        self.language_combo = QtWidgets.QComboBox()
        self.language_combo.addItems(["English", "Tiếng Việt", "日本語"])
        self.language_combo.setCurrentIndex(0)
        self.language_combo.currentIndexChanged.connect(self.change_language)
        self.language_combo.setView(QtWidgets.QListView())
        self.language_combo.setMaxVisibleItems(5)
        class_management_layout.addWidget(language_label)
        class_management_layout.addWidget(self.language_combo)

        self.class_management_group.setLayout(class_management_layout)
        control_layout.addWidget(self.class_management_group)

        # Student management
        self.student_management_group = QtWidgets.QGroupBox(TRANSLATIONS[self.current_language]["student_management"])
        student_management_layout = QtWidgets.QVBoxLayout()

        self.add_student_button = AnimatedButton(TRANSLATIONS[self.current_language]["add_new_student"],
                                                 icon_path="add_student_icon.png")
        self.add_student_button.clicked.connect(self.add_student)
        student_management_layout.addWidget(self.add_student_button)

        self.search_button = AnimatedButton(TRANSLATIONS[self.current_language]["search_and_delete"],
                                            icon_path="search_icon.png")
        self.search_button.clicked.connect(self.search_student)
        student_management_layout.addWidget(self.search_button)

        self.student_management_group.setLayout(student_management_layout)
        control_layout.addWidget(self.student_management_group)

        # Attendance
        self.attendance_group = QtWidgets.QGroupBox(TRANSLATIONS[self.current_language]["attendance"])
        attendance_layout = QtWidgets.QVBoxLayout()

        self.mark_attendance_button = AnimatedButton(TRANSLATIONS[self.current_language]["mark_attendance"],
                                                     icon_path="attendance_icon.png")
        self.mark_attendance_button.clicked.connect(self.mark_attendance_dialog)
        attendance_layout.addWidget(self.mark_attendance_button)

        self.view_attendance_button = AnimatedButton(TRANSLATIONS[self.current_language]["view_attendance"],
                                                     icon_path="view_icon.png")
        self.view_attendance_button.clicked.connect(self.view_attendance)
        attendance_layout.addWidget(self.view_attendance_button)

        self.attendance_group.setLayout(attendance_layout)
        control_layout.addWidget(self.attendance_group)

        control_layout.addStretch()
        main_layout.addWidget(self.control_frame, 1)

        # Attendance records
        self.attendance_frame = QtWidgets.QGroupBox(TRANSLATIONS[self.current_language]["attendance_records"])
        attendance_frame_layout = QtWidgets.QVBoxLayout()
        self.attendance_frame.setLayout(attendance_frame_layout)

        self.attendance_table = QtWidgets.QTableWidget()
        self.attendance_table.setMinimumHeight(600)
        attendance_frame_layout.addWidget(self.attendance_table)

        main_layout.addWidget(self.attendance_frame, 3)

        if self.class_combo.count() > 0:
            self.current_class = self.class_combo.currentText()
            self.load_class_data()

        self.update_stylesheet()
        self.update_ui_state()

        combo_style = """
            QComboBox {
                background: rgba(255, 255, 255, 0.15);
                border: 2px solid #60A5FA;
                border-radius: 20px;
                padding: 6px 30px 6px 10px;
                color: white;
                font-weight: bold;
                min-width: 120px;
                max-height: 40px;
            }
            QComboBox:hover {
                border: 2px solid #3B82F6;
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
                border: 2px solid #3B82F6;
                border-radius: 10px;
                color: white;
                selection-background-color: #2563EB;
                padding: 5px;
                margin: 0px;
            }
            QComboBox QAbstractItemView::item {
                height: 30px;
                padding: 5px;
                border: none;
            }
        """
        self.class_combo.setStyleSheet(combo_style)
        self.language_combo.setStyleSheet(combo_style)

    def style_dialog(self, dialog, custom_stylesheet=None):
        if custom_stylesheet:
            dialog.setStyleSheet(custom_stylesheet)
        else:
            dialog.setStyleSheet(get_main_stylesheet())
        for button in dialog.findChildren(AnimatedButton):
            button.setStyleSheet("""
                AnimatedButton {
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                }
            """)

    def change_language(self, index):
        if index == 0:
            self.current_language = "en"
        elif index == 1:
            self.current_language = "vi"
        else:
            self.current_language = "jp"
        self.update_ui_language()

    def update_ui_language(self):
        self.setWindowTitle(TRANSLATIONS[self.current_language]["app_title"])
        self.control_frame.setTitle(TRANSLATIONS[self.current_language]["controls"])
        self.class_management_group.setTitle(TRANSLATIONS[self.current_language]["class_management"])
        self.student_management_group.setTitle(TRANSLATIONS[self.current_language]["student_management"])
        self.attendance_group.setTitle(TRANSLATIONS[self.current_language]["attendance"])
        self.add_class_button.setText(TRANSLATIONS[self.current_language]["add_new_class"])
        self.delete_class_button.setText(TRANSLATIONS[self.current_language]["delete_current_class"])
        self.add_student_button.setText(TRANSLATIONS[self.current_language]["add_new_student"])
        self.search_button.setText(TRANSLATIONS[self.current_language]["search_and_delete"])
        self.mark_attendance_button.setText(TRANSLATIONS[self.current_language]["mark_attendance"])
        self.view_attendance_button.setText(TRANSLATIONS[self.current_language]["view_attendance"])
        self.attendance_frame.setTitle(TRANSLATIONS[self.current_language]["attendance_records"])
        self.load_class_data()

    def load_class_data(self):
        if self.current_class:
            self.known_face_encodings, self.known_face_ids, self.known_face_names = load_known_faces(self.current_class)
            initialize_attendance(self.current_class)
            self.attendance_frame.setTitle(
                f"{TRANSLATIONS[self.current_language]['attendance_records']} - {self.current_class}")
            self.view_attendance()

    def change_class(self):
        self.current_class = self.class_combo.currentText()
        self.load_class_data()
        self.update_ui_state()

    def update_ui_state(self):
        has_class = self.current_class is not None
        self.delete_class_button.setEnabled(has_class)
        self.add_student_button.setEnabled(has_class)
        self.mark_attendance_button.setEnabled(has_class)
        self.view_attendance_button.setEnabled(has_class)

    def add_class(self):
        dialog = QtWidgets.QInputDialog(self)
        dialog.setWindowTitle(TRANSLATIONS[self.current_language]["add_class_title"])
        dialog.setLabelText(TRANSLATIONS[self.current_language]["enter_class_name"])
        dialog.setOkButtonText(TRANSLATIONS[self.current_language]["add"])
        dialog.setCancelButtonText(TRANSLATIONS[self.current_language]["cancel"])
        self.style_dialog(dialog)

        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            class_name = dialog.textValue().strip()
            if class_name:
                if add_class(class_name):
                    self.class_combo.clear()
                    self.class_combo.addItems(get_all_classes())
                    self.class_combo.setCurrentText(class_name)
                    self.current_class = class_name
                    self.load_class_data()
                    self.update_ui_state()
                else:
                    msg = QtWidgets.QMessageBox(self)
                    msg.setWindowTitle(TRANSLATIONS[self.current_language]["error"])
                    msg.setText(TRANSLATIONS[self.current_language]["class_exists"])
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    self.style_dialog(msg)
                    msg.exec()

    def delete_class(self):
        if not self.current_class:
            return

        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle(TRANSLATIONS[self.current_language]["confirm_delete"])
        msg.setText(TRANSLATIONS[self.current_language]["delete_class_confirm"].format(class_name=self.current_class))
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        yes_button = msg.addButton(TRANSLATIONS[self.current_language]["yes"],
                                   QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        no_button = msg.addButton(TRANSLATIONS[self.current_language]["no"],
                                  QtWidgets.QMessageBox.ButtonRole.RejectRole)
        self.style_dialog(msg)
        msg.exec()

        if msg.clickedButton() == yes_button:
            if delete_class(self.current_class):
                import shutil
                class_dir, _ = get_class_folder(self.current_class)
                shutil.rmtree(class_dir, ignore_errors=True)

                self.class_combo.clear()
                classes = get_all_classes()
                self.class_combo.addItems(classes)

                if classes:
                    self.current_class = classes[0]
                    self.class_combo.setCurrentText(self.current_class)
                    self.load_class_data()
                else:
                    self.current_class = None
                    self.attendance_table.clear()
                    self.attendance_table.setRowCount(0)
                    self.attendance_table.setColumnCount(0)
                    self.attendance_frame.setTitle(TRANSLATIONS[self.current_language]["attendance_records"])

                self.update_ui_state()

    def add_student(self):
        if not self.current_class:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle(TRANSLATIONS[self.current_language]["error"])
            msg.setText(TRANSLATIONS[self.current_language]["select_class_first"])
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.style_dialog(msg)
            msg.exec()
            return

        dialog = AddStudentDialog(self)
        dialog.class_combo.setCurrentText(self.current_class)
        self.style_dialog(dialog, get_add_student_stylesheet())
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.load_class_data()

    def mark_attendance_dialog(self):
        if not self.current_class:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowliches.QMessageBox(self)
            msg.setWindowTitle(TRANSLATIONS[self.current_language]["error"])
            msg.setText(TRANSLATIONS[self.current_language]["select_class_first"])
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.style_dialog(msg)
            msg.exec()
            return

        dialog = MarkAttendanceDialog(self)
        self.style_dialog(dialog, get_mark_attendance_stylesheet())
        dialog.exec()

    def delete_student(self):
        if not self.current_class:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle(TRANSLATIONS[self.current_language]["error"])
            msg.setText(TRANSLATIONS[self.current_language]["select_class_first"])
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.style_dialog(msg)
            msg.exec()
            return

        if not hasattr(self, 'known_face_ids') or not self.known_face_ids:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle(TRANSLATIONS[self.current_language]["error"])
            msg.setText(TRANSLATIONS[self.current_language]["no_students_to_delete"])
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.style_dialog(msg)
            msg.exec()
            return

        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle(TRANSLATIONS[self.current_language]["delete_student_title"])
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(TRANSLATIONS[self.current_language]["select_student_to_delete"])
        layout.addWidget(label)

        student_combo = QtWidgets.QComboBox()
        for student_id, name in zip(self.known_face_ids, self.known_face_names):
            student_combo.addItem(f"{student_id} - {name}")
        student_combo.setView(QtWidgets.QListView())
        student_combo.setMaxVisibleItems(10)
        layout.addWidget(student_combo)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(lambda: self.confirm_delete(student_combo.currentText(), dialog))
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        dialog.setLayout(layout)
        self.style_dialog(dialog)

        student_combo.setStyleSheet("""
            QComboBox {
                background: rgba(255, 255, 255, 0.15);
                border: 2px solid #60A5FA;
                border-radius: 20px;
                padding: 6px 30px 6px 10px;
                color: white;
                font-weight: bold;
                min-width: 120px;
                max-height: 40px;
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
                border: 2px solid #3B82F6;
                border-radius: 10px;
                color: white;
                selection-background-color: #2563EB;
                padding: 5px;
                margin: 0px;
            }
            QComboBox QAbstractItemView::item {
                height: 30px;
                padding: 5px;
                border: none;
            }
        """)
        dialog.exec()

    def search_student(self):
        if not self.current_class:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle(TRANSLATIONS[self.current_language]["error"])
            msg.setText(TRANSLATIONS[self.current_language]["select_class_first"])
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            self.style_dialog(msg)
            msg.exec()
            return

        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle(TRANSLATIONS[self.current_language]["search_and_delete"])
        dialog.setFixedSize(600, 500)
        layout = QtWidgets.QVBoxLayout()

        search_layout = QtWidgets.QHBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText(TRANSLATIONS[self.current_language]["student_name"])
        search_button = AnimatedButton(TRANSLATIONS[self.current_language]["search"], icon_path="search_icon.png")
        search_button.clicked.connect(lambda: self.perform_search(dialog))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.results_table = QtWidgets.QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels([
            TRANSLATIONS[self.current_language]["student_number"],
            TRANSLATIONS[self.current_language]["student_id"],
            TRANSLATIONS[self.current_language]["name"],
            TRANSLATIONS[self.current_language]["delete_action"]
        ])
        self.results_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.results_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        layout.addWidget(self.results_table)

        dialog.setLayout(layout)
        self.style_dialog(dialog)
        dialog.exec()

    def perform_search(self, dialog):
        search_term = self.search_input.text().lower()
        if not search_term:
            QtWidgets.QMessageBox.information(
                dialog,
                TRANSLATIONS[self.current_language]["search_and_delete"],
                "Please enter a search term",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            return

        attendance_file = get_class_attendance_file(self.current_class)
        try:
            with open(attendance_file, 'r') as f:
                data = json.load(f)
        except:
            data = {}

        self.results_table.setRowCount(0)

        filtered_students = [(sid, sdata) for sid, sdata in data.items()
                             if search_term in sdata["name"].lower()]
        sorted_students = sorted(filtered_students, key=lambda x: x[1]["name"].lower())

        for row, (student_id, student_data) in enumerate(sorted_students):
            self.results_table.insertRow(row)
            self.results_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row + 1)))
            self.results_table.setItem(row, 1, QtWidgets.QTableWidgetItem(student_id))
            self.results_table.setItem(row, 2, QtWidgets.QTableWidgetItem(student_data["name"]))

            delete_button = AnimatedButton(TRANSLATIONS[self.current_language]["delete"], icon_path="delete_icon.png")
            delete_button.setFixedWidth(100)  # Increased width
            delete_button.clicked.connect(lambda _, sid=student_id, sname=student_data["name"]:
                                          self.confirm_delete_from_search(sid, sname, dialog))
            self.results_table.setCellWidget(row, 3, delete_button)

        if not sorted_students:
            self.results_table.setRowCount(1)
            self.results_table.setItem(0, 0,
                                       QtWidgets.QTableWidgetItem(TRANSLATIONS[self.current_language]["no_results"]))
            self.results_table.setSpan(0, 0, 1, 4)

    def confirm_delete_from_search(self, student_id, student_name, dialog):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle(TRANSLATIONS[self.current_language]["search_and_delete"] + " - Confirmation")
        msg.setText(
            f"{TRANSLATIONS[self.current_language]['delete_student_confirm'].format(name=student_name, student_id=student_id)}\n\nThis action cannot be undone.")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        yes_button = msg.addButton(TRANSLATIONS[self.current_language]["yes"],
                                   QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        no_button = msg.addButton(TRANSLATIONS[self.current_language]["no"],
                                  QtWidgets.QMessageBox.ButtonRole.RejectRole)
        self.style_dialog(msg)
        msg.exec()

        if msg.clickedButton() == yes_button:
            _, faces_dir = get_class_folder(self.current_class)
            for i in range(3):
                img_path = os.path.join(faces_dir, f"{student_id}_{student_name}_{i}.jpg")
                if os.path.exists(img_path):
                    os.remove(img_path)

            attendance_file = get_class_attendance_file(self.current_class)
            try:
                with open(attendance_file, 'r') as f:
                    data = json.load(f)

                if student_id in data:
                    del data[student_id]

                with open(attendance_file, 'w') as f:
                    json.dump(data, f, indent=4)
            except Exception as e:
                print(f"Error deleting student: {e}")

            self.load_class_data()
            self.perform_search(dialog)

    def confirm_delete(self, selected_student, dialog):
        if not selected_student:
            return

        student_id, name = selected_student.split(" - ", 1)

        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle(TRANSLATIONS[self.current_language]["confirm_deletion"])
        msg.setText(
            TRANSLATIONS[self.current_language]["delete_student_confirm"].format(name=name, student_id=student_id))
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        yes_button = msg.addButton(TRANSLATIONS[self.current_language]["yes"],
                                   QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        no_button = msg.addButton(TRANSLATIONS[self.current_language]["no"],
                                  QtWidgets.QMessageBox.ButtonRole.RejectRole)
        self.style_dialog(msg)
        msg.exec()

        if msg.clickedButton() == yes_button:
            _, faces_dir = get_class_folder(self.current_class)
            for i in range(3):
                img_path = os.path.join(faces_dir, f"{student_id}_{name}_{i}.jpg")
                if os.path.exists(img_path):
                    os.remove(img_path)

            attendance_file = get_class_attendance_file(self.current_class)
            try:
                with open(attendance_file, 'r') as f:
                    data = json.load(f)

                if student_id in data:
                    del data[student_id]

                with open(attendance_file, 'w') as f:
                    json.dump(data, f, indent=4)
            except Exception as e:
                print(f"Error deleting student: {e}")

            self.load_class_data()

        dialog.accept()

    def view_attendance(self):
        if not self.current_class:
            return

        attendance_file = get_class_attendance_file(self.current_class)
        try:
            with open(attendance_file, 'r') as f:
                data = json.load(f)
        except:
            data = {}

        if not data:
            self.attendance_table.clear()
            self.attendance_table.setRowCount(0)
            self.attendance_table.setColumnCount(0)
            return

        sorted_students = sorted(data.items(), key=lambda x: x[1]["name"].lower())

        all_dates = set()
        for student_id, student_data in sorted_students:
            all_dates.update(student_data["attendance"].keys())

        if not all_dates:
            self.attendance_table.clear()
            self.attendance_table.setRowCount(0)
            self.attendance_table.setColumnCount(0)
            return

        date_objects = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in all_dates]
        sorted_dates = sorted(date_objects, reverse=True)[:30]
        formatted_dates = [date.strftime("%d/%m/%Y") for date in sorted_dates]

        headers = [TRANSLATIONS[self.current_language]["student_id"],
                   TRANSLATIONS[self.current_language]["name"]] + formatted_dates

        self.attendance_table.setColumnCount(len(headers))
        self.attendance_table.setHorizontalHeaderLabels(headers)

        self.attendance_table.setRowCount(len(sorted_students))

        for row, (student_id, student_data) in enumerate(sorted_students):
            self.attendance_table.setItem(row, 0, QtWidgets.QTableWidgetItem(student_id))
            name_item = QtWidgets.QTableWidgetItem(student_data["name"])
            name_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.attendance_table.setItem(row, 1, name_item)

            for col, date_obj in enumerate(sorted_dates, start=2):
                date_str = date_obj.strftime("%Y-%m-%d")
                attended = student_data["attendance"].get(date_str, False)
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.CheckState.Checked if attended else QtCore.Qt.CheckState.Unchecked)
                item.setBackground(QtGui.QColor("#28a745" if attended else "#d9534f"))
                self.attendance_table.setItem(row, col, item)

        self.attendance_table.setColumnWidth(1, 200)
        self.attendance_table.resizeColumnsToContents()
        self.attendance_table.resizeRowsToContents()

    def update_stylesheet(self):
        stylesheet = get_main_stylesheet()
        self.setStyleSheet(stylesheet)
        self.control_frame.setStyleSheet(stylesheet)
        self.class_management_group.setStyleSheet(stylesheet)
        self.student_management_group.setStyleSheet(stylesheet)
        self.attendance_group.setStyleSheet(stylesheet)
        self.attendance_frame.setStyleSheet(stylesheet)
        self.attendance_table.setStyleSheet(stylesheet)

    def closeEvent(self, event):
        event.accept()

def main():
    app = QtWidgets.QApplication([])

    login_dialog = LoginDialog()
    login_dialog.setStyleSheet(get_login_stylesheet())
    if login_dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
        return

    window = FaceAttendanceApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()