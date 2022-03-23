"""Listing 16-3
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QVBoxLayout)
from PyQt6.QtCore import Qt, QDate, QTime, QTimer

class DisplayTime(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle("16.3 – QDateTime Example")
        self.setStyleSheet("background-color: black")

        self.setUpMainWindow()

        # Create timer object
        timer = QTimer(self)
        timer.timeout.connect(self.updateDateTime)
        timer.start(1000) 

        self.show()

    def setUpMainWindow(self):
        """Create labels that will display current date and 
        time in the main window."""
        current_date, current_time = self.getDateTime()

        self.date_label = QLabel(current_date)
        self.date_label.setStyleSheet("color: white; font: 16px Courier")
        self.time_label = QLabel(current_time)
        self.time_label.setStyleSheet("""color: white;
                                         border-color: white;
                                         border-width: 2px; 
                                         border-style: solid;
                                         border-radius: 4px;
                                         padding: 10px; 
                                         font: bold 24px Courier""")

        # Create layout and add widgets
        v_box = QVBoxLayout()
        v_box.addWidget(self.date_label, alignment=Qt.AlignmentFlag.AlignCenter)
        v_box.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(v_box)
    
    def getDateTime(self):
        """Returns current date and time."""
        date = QDate.currentDate().toString("MMMM dd, yyyy")
        time = QTime.currentTime().toString("hh:mm:ss AP") 
        return date, time

    def updateDateTime(self):
        """Slot that updates date and time values."""
        date = QDate.currentDate().toString("MMMM dd, yyyy")
        time = QTime.currentTime().toString("hh:mm:ss AP")

        self.date_label.setText(date)
        self.time_label.setText(time)
        return date, time

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayTime()
    sys.exit(app.exec())