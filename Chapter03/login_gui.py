"""Listing 3-14 to Listing 3-22
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
     QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from registration import NewUserDialog     

class LoginWindow(QWidget):
    
    def __init__(self): 
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(360, 220)
        self.setWindowTitle("3.1 – Login GUI")

        self.setUpWindow()
        self.show()

    def setUpWindow(self):
        """Create and arrange widgets in the main window."""
        self.login_is_successful = False

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)

        # Create widgets for username and password 
        username_label = QLabel("Username:", self)
        username_label.move(20, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.resize(250, 24)
        self.username_edit.move(90, 50)

        password_label = QLabel("Password:", self)
        password_label.move(20, 86)

        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)
        
        # Create QCheckBox for displaying password
        self.show_password_cb = QCheckBox("Show Password", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        # Create QPushButton for signing in
        login_button = QPushButton("Login", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        # Create sign up QLabel and QPushButton
        not_member_label = QLabel("Not a member?", self)
        not_member_label.move(20, 186)

        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        """Check if username and password match any existing 
        entries in users.txt. 
        If they exist, display QMessageBox and close program. 
        If they don't, display a warning QMessageBox."""
        users = {} # Dictionary to store user information
        file = "files/users.txt"

        try:
            with open(file, 'r') as f:
                for line in f:
                    user_info = line.split(" ")
                    username_info = user_info[0]
                    password_info = user_info[1].strip('\n')
                    users[username_info] = password_info

            # Collect user and password information
            username = self.username_edit.text()
            password = self.password_edit.text()

            if (username, password) in users.items():
                QMessageBox.information(self, "Login Successful!", 
                    "Login Successful!", QMessageBox.StandardButton.Ok, 
                    QMessageBox.StandardButton.Ok)
                self.login_is_successful = True
                self.close() # Close the login window
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, "Error Message",
                    "The username or password is incorrect.", 
                    QMessageBox.StandardButton.Close, 
                    QMessageBox.StandardButton.Close)
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error",
                f"""<p>File not found.</p> 
                <p>Error: {error}</p>""", 
                QMessageBox.StandardButton.Ok)
            # Create file if it doesn't exist
            f = open(file, "w")

    def displayPasswordIfChecked(self, checked):
        """If QCheckButton is enabled, view password.
        Else, mask the password so others can not see it."""
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def createNewUser(self):
        """Open a dialog for creating a new account."""
        self.create_new_user_window = NewUserDialog()
        self.create_new_user_window.show()

    def openApplicationWindow(self):
        """Open a mock main window after the user logs in."""
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        """Reimplement the closing event to display a QMessageBox
        before closing."""
        if self.login_is_successful == True:
            event.accept()
        else:
            answer = QMessageBox.question(self, "Quit Application?",
                "Are you sure you want to QUIT?", 
                QMessageBox.StandardButton.No | \
                QMessageBox.StandardButton.Yes, 
                QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            if answer == QMessageBox.StandardButton.No:
                event.ignore() 

class MainWindow(QWidget):

    def __init__(self): 
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(640, 426)
        self.setWindowTitle("3.1 – Main Window")
        self.setUpMainWindow()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        image = "images/background_kingfisher.jpg"

        try:
            with open(image):
                main_label = QLabel(self)
                pixmap = QPixmap(image)
                main_label.setPixmap(pixmap)
                main_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())