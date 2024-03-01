import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Buttons, Ui
from dotenv import load_dotenv

# Load environment variables from .env file (login credentials)
load_dotenv()

class Ui_MainWindow(QMainWindow, Ui, Buttons):
    
    # Default values or values obtained from environment variables
    MASTERLOGIN = os.environ.get('MASTERLOGIN', '1')
    MASTERPASS = os.environ.get('MASTERPASS', '1')
    
    def __init__(self):
        super().__init__()
        
        # Set up the UI components and features
        self.setupUi(self)
        self.button_features()

if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create an instance of the main window
    window = Ui_MainWindow()
    window.show()

    # Execute the application event loop and handle exit codes
    sys.exit(app.exec_())