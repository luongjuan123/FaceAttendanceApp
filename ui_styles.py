def get_main_stylesheet():
    return """
        QWidget {
            background: #1a1b26;
            font-family: "Segoe UI", "Arial", sans-serif;
            font-weight: bold;
            font-size: 14px;
            color: #a9b1d6;
        }

        QGroupBox {
            border: 2px solid #414868;
            border-radius: 15px;
            margin-top: 10px;
            background-color: #24283b;
            padding: 10px;
            font-size: 16px;
            color: #7aa2f7;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 5px;
            color: #7aa2f7;
            font-size: 18px;
            font-weight: bold;
        }

        QPushButton {
            background-color: #7aa2f7;
            color: #1a1b26;
            border: none;
            border-radius: 15px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }

        QPushButton:hover {
            background-color: #9aa5ce;
        }

        QPushButton:pressed {
            background-color: #565f89;
        }

        QComboBox {
            background: #24283b;
            border: 2px solid #414868;
            border-radius: 8px;
            padding: 4px 10px 4px 10px;
            color: #a9b1d6;
            font-weight: bold;
            min-width: 80px;
            height: 28px;
            font-size: 12px;
        }

        QComboBox:hover {
            border: 2px solid #7aa2f7;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border: none;
            background: transparent;
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
        }

        QComboBox::down-arrow {
            image: url(down_arrow.png);
            width: 10px;
            height: 10px;
        }

        QComboBox QAbstractItemView {
            background: #24283b;
            border: 2px solid #7aa2f7;
            border-radius: 6px;
            color: #a9b1d6;
            selection-background-color: #7aa2f7;
            selection-color: #1a1b26;
            padding: 2px;
            outline: 0;
            min-width: 100px;
            font-size: 12px;
        }

        QComboBox QAbstractItemView::item {
            height: 24px;
            padding: 2px 8px;
            border: none;
        }

        QDialog#mark_attendance_dialog {
            background: #1a1b26;
            border: 2px solid #7aa2f7;
            border-radius: 15px;
        }

        QLabel#camera_label {
            background: #24283b;
            border: 1px solid #414868;
            border-radius: 10px;
            padding: 5px;
        }

        QLabel#status_label {
            color: #7aa2f7;
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
        }

        QScrollBar:vertical {
            background: #24283b;
            width: 12px;
            margin: 0px;
            border: none;
            border-radius: 6px;
        }

        QScrollBar::handle:vertical {
            background: #7aa2f7;
            min-height: 30px;
            border-radius: 6px;
        }

        QScrollBar::add-line:vertical, 
        QScrollBar::sub-line:vertical {
            height: 0px;
            background: none;
        }

        QScrollBar::add-page:vertical, 
        QScrollBar::sub-page:vertical {
            background: #24283b;
        }

        QScrollBar:horizontal {
            background: #24283b;
            height: 12px;
            margin: 0px;
            border: none;
            border-radius: 6px;
        }

        QScrollBar::handle:horizontal {
            background: #7aa2f7;
            min-width: 30px;
            border-radius: 6px;
        }

        QScrollBar::add-line:horizontal, 
        QScrollBar::sub-line:horizontal {
            width: 0px;
            background: none;
        }

        QScrollBar::add-page:horizontal, 
        QScrollBar::sub-page:horizontal {
            background: #24283b;
        }

        QTableWidget {
            background: #24283b;
            border: 1px solid #414868;
            border-radius: 12px;
            gridline-color: #414868;
            padding: 5px;
            margin: 0px;
            font-weight: bold;
            overflow: hidden;
        }

        QTableWidget::item {
            border: 1px solid #414868;
            color: #a9b1d6;
            background: #1a1b26;
            font-weight: bold;
            padding: 5px;
        }

        QTableWidget::item:selected {
            background-color: #7aa2f7;
            color: #1a1b26;
            border-radius: 5px;
        }

        QHeaderView::section {
            background-color: #414868;
            color: #a9b1d6;
            padding: 5px;
            border: 1px solid #414868;
            font-size: 14px;
            font-weight: bold;
        }

        QLabel {
            color: #a9b1d6;
            font-size: 14px;
            font-weight: bold;
            border: none;
        }

        QLineEdit {
            background-color: #24283b;
            border: 2px solid #414868;
            border-radius: 15px;
            padding: 10px;
            color: #a9b1d6;
            font-size: 14px;
            font-weight: bold;
        }

        QLineEdit:focus {
            border: 2px solid #7aa2f7;
            background-color: #1a1b26;
            color: #a9b1d6;
        }
    """

def get_login_stylesheet():
    return """
        QDialog {
            background: #1a1b26;
            font-family: "Segoe UI", "Arial", sans-serif;
            font-weight: bold;
            font-size: 14px;
            border-radius: 25px;
        }

        QLineEdit {
            background-color: #24283b;
            border: 2px solid #414868;
            border-radius: 15px;
            padding: 10px;
            color: #a9b1d6;
            font-size: 14px;
            font-weight: bold;
        }

        QLineEdit:focus {
            border: 2px solid #7aa2f7;
            background-color: #1a1b26;
            color: #a9b1d6;
        }

        QPushButton {
            background-color: #7aa2f7;
            color: #1a1b26;
            border: none;
            border-radius: 15px;
            padding: 12px;
            font-weight: bold;
            font-size: 16px;
        }

        QPushButton:hover {
            background-color: #9aa5ce;
        }

        QPushButton:pressed {
            background-color: #565f89;
        }

        QCheckBox {
            color: #a9b1d6;
            font-size: 14px;
        }

        QCheckBox::indicator {
            width: 16px;
            height: 16px;
            border: 2px solid #7aa2f7;
            background-color: #24283b;
        }

        QCheckBox::indicator:checked {
            background-color: #7aa2f7;
        }

        QLabel {
            color: #565f89;
            font-size: 14px;
        }
    """

def get_add_student_stylesheet():
    return """
        QDialog {
            background: #1a1b26;
            font-family: "Segoe UI", "Arial", sans-serif;
            font-weight: bold;
            font-size: 14px;
            border-radius: 25px;
        }

        QLineEdit {
            background-color: #24283b;
            border: 2px solid #414868;
            border-radius: 15px;
            padding: 10px;
            color: #a9b1d6;
            font-size: 14px;
            font-weight: bold;
        }

        QLineEdit:focus {
            border: 2px solid #7aa2f7;
            background-color: #1a1b26;
            color: #a9b1d6;
        }

        QComboBox {
            background: #7aa2f7;
            border: none;
            border-radius: 8px;
            padding: 4px 10px 4px 10px;
            color: #1a1b26;
            font-weight: bold;
            font-size: 12px;
            min-width: 80px;
            height: 28px;
        }

        QComboBox:hover {
            background-color: #9aa5ce;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border: none;
            background: transparent;
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
        }

        QComboBox::down-arrow {
            image: url(down_arrow.png);
            width: 10px;
            height: 10px;
        }

        QComboBox QAbstractItemView {
            background: #24283b;
            border: 2px solid #7aa2f7;
            border-radius: 6px;
            color: #a9b1d6;
            selection-background-color: #7aa2f7;
            selection-color: #1a1b26;
            padding: 2px;
            outline: 0;
            min-width: 100px;
            font-size: 12px;
            scrollbar: vertical;
            max-height: 200px;
        }

        QComboBox QAbstractItemView::item {
            height: 24px;
            padding: 2px 8px;
            border: none;
        }

        QPushButton {
            background-color: #7aa2f7;
            color: #1a1b26;
            border: none;
            border-radius: 15px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }

        QPushButton:hover {
            background-color: #9aa5ce;
        }

        QPushButton:pressed {
            background-color: #565f89;
        }

        QPushButton:disabled {
            background-color: #565f89;
            color: #414868;
        }

        QLabel {
            color: #a9b1d6;
            font-size: 14px;
            border: none;
        }

        QScrollBar:vertical {
            background: #24283b;
            width: 12px;
            border-left: 1px solid #414868;
        }

        QScrollBar::handle:vertical {
            background: #7aa2f7;
            min-height: 30px;
            border-radius: 6px;
            margin: 2px;
        }

        QScrollBar::add-line:vertical, 
        QScrollBar::sub-line:vertical {
            background: #414868;
            height: 10px;
        }

        QScrollBar::add-page:vertical, 
        QScrollBar::sub-page:vertical {
            background: #24283b;
        }
    """

def get_mark_attendance_stylesheet():
    return """
        QDialog {
            background: #1a1b26;
            font-family: "Poppins", Arial, sans-serif;
            font-size: 14px;
            border-radius: 25px;
        }

        QPushButton {
            background-color: #7aa2f7;
            color: #1a1b26;
            border: none;
            border-radius: 15px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }

        QPushButton:hover {
            background-color: #9aa5ce;
        }

        QPushButton:pressed {
            background-color: #565f89;
        }

        QLabel {
            color: #a9b1d6;
            font-size: 14px;
            border: none;
        }
    """

def get_capture_stylesheet():
    return """
        QDialog {
            background: #1a1b26;
            font-family: "Segoe UI", "Arial", sans-serif;
            font-weight: bold;
            font-size: 14px;
            border: 2px solid #414868;
            border-radius: 15px;
        }
        QGroupBox {
            border: 2px solid #414868;
            border-radius: 10px;
            background-color: #24283b;
            padding: 10px;
            color: #7aa2f7;
            font-size: 16px;
            font-weight: bold;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 5px;
        }
        QLabel {
            color: #a9b1d6;
            font-size: 14px;
            font-weight: bold;
            border: none;
        }
        QPushButton {
            background-color: #7aa2f7;
            color: #1a1b26;
            border: none;
            border-radius: 15px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #9aa5ce;
        }
        QPushButton:pressed {
            background-color: #565f89;
        }
    """

def get_mark_capture_stylesheet():
    return """
        QDialog {
            background: #1a1b26;
            font-family: "Segoe UI", "Arial", sans-serif;
            font-weight: bold;
            font-size: 14px;
            border: 2px solid #414868;
            border-radius: 15px;
        }
        QLabel {
            color: #a9b1d6;
            font-size: 16px;
            font-weight: bold;
            border: none;
        }
        QLabel#camera_label {
            background: #24283b;
            border: 2px solid #414868;
            border-radius: 12px;
            padding: 5px;
        }
        QLabel#status_label {
            color: #7aa2f7;
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
        }
        QPushButton {
            background-color: #7aa2f7;
            color: #1a1b26;
            border: none;
            border-radius: 15px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #9aa5ce;
        }
        QPushButton:pressed {
            background-color: #565f89;
        }
    """