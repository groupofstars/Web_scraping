import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set window title and geometry
        self.setWindowTitle("Web Search")
        self.setGeometry(100, 100, 400, 300)
        
        # Create UI widgets
        url_label = QLabel("Enter URL:")
        self.url_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.cancel_button = QPushButton("Cancel")
        self.search_result_label = QLabel("Search Results")
        
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.search_result_label)
        
        # Set the layout for the window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())