import sys
from PyQt5 import QtWidgets, QtGui
from collections import Counter

class DuplicateLineDetector(QtWidgets.QMainWindow):
    def __init__(self):
        super(DuplicateLineDetector, self).__init__()

        # Set window title, icon, size, and position (centered at 1024x1024)
        self.setWindowTitle("Duplicate Line Detector")
        self.setWindowIcon(QtGui.QIcon(r"C:\Users\your_pc_name\Downloads\Text_Duplicate\icon.ico"))
        self.resize(1024, 1024)
        self.center()

        # Set layout
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Original Text Area
        self.original_label = QtWidgets.QLabel("Original Text: 0 lines")
        self.layout.addWidget(self.original_label)
        self.text_original = QtWidgets.QPlainTextEdit(self)
        self.layout.addWidget(self.text_original)

        # Results Text Area
        self.results_label = QtWidgets.QLabel("Results After Removing Duplicates: 0 lines")
        self.layout.addWidget(self.results_label)
        self.text_results = QtWidgets.QPlainTextEdit(self)
        self.text_results.setReadOnly(True)
        self.layout.addWidget(self.text_results)

        # Buttons
        self.remove_button = QtWidgets.QPushButton("Remove Duplicates", self)
        self.clear_button = QtWidgets.QPushButton("Clear", self)
        self.layout.addWidget(self.remove_button)
        self.layout.addWidget(self.clear_button)

        # Connect buttons to functions
        self.remove_button.clicked.connect(self.remove_duplicates)
        self.clear_button.clicked.connect(self.clear_text)

        # Connect real-time update for line counts
        self.text_original.textChanged.connect(self.update_counts)

    def center(self):
        """Center the window on the screen."""
        frame_geometry = self.frameGeometry()
        screen_center = QtWidgets.QApplication.desktop().screenGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def remove_duplicates(self):
        """Removes duplicates and updates results with unique lines."""
        input_text = self.text_original.toPlainText().strip()
        lines = input_text.splitlines()

        # Count occurrences and find duplicates
        line_count = Counter(lines)
        unique_lines = [line for line, count in line_count.items() if count == 1]

        # Display results
        if unique_lines:
            self.text_results.setPlainText("\n".join(unique_lines))
        else:
            self.text_results.setPlainText("No duplicates found.")

        # Update line counts
        self.update_counts()

    def clear_text(self):
        """Clears both text areas and resets labels."""
        self.text_original.clear()
        self.text_results.clear()
        self.update_counts()

    def update_counts(self):
        """Updates line counts in real-time as text is changed."""
        input_text = self.text_original.toPlainText().strip()
        lines = input_text.splitlines()
        unique_lines = set(lines)

        # Update labels with line counts
        self.original_label.setText(f"Original Text: {len(lines)} lines")
        self.results_label.setText(f"Results After Removing Duplicates: {len(unique_lines)} lines")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DuplicateLineDetector()
    window.show()
    sys.exit(app.exec_())
