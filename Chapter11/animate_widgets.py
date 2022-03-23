"""Listing 11-28 to Listing 11-31
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
    QPushButton, QCheckBox, QVBoxLayout)
from PyQt6.QtCore import (QAbstractAnimation, QRect, QSize, 
    QPoint, QEasingCurve, pyqtProperty,
    QPropertyAnimation, QSequentialAnimationGroup)
from PyQt6.QtGui import QColor

class AnimatedCheckbox(QCheckBox):

    def __init__(self, text):
        """Custom QCheckBox with animated text."""
        super().__init__(text)

    def _set_color(self, color):
        """Method for the color property of the text using 
        style sheets."""
        self.setStyleSheet(
            f"""color: rgb({color.red()}, {color.green()}, 
                {color.blue()})""")

    color = pyqtProperty(QColor, fset=_set_color)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(240, 120)
        self.setWindowTitle("Animating Widgets")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.update_cb = AnimatedCheckbox("Normal")
        self.update_cb.stateChanged.connect(self.stopFlashing)

        self.status_button = QPushButton("Status Changed")
        self.status_button.clicked.connect(self.startAnimations)

        # Create animation instances
        self.cb_anim = QPropertyAnimation(self.update_cb, b"color")
        self.button_anim = QPropertyAnimation(self.status_button, b"geometry")
        self.seq_group = QSequentialAnimationGroup()

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.update_cb)
        main_v_box.addWidget(self.status_button)
        self.setLayout(main_v_box)

    def startAnimations(self):
        """Play the animations and update the states of the widgets."""
        # Collect the button's initial geometry values.
        # start_geometry is a QRect object
        start_geometry = self.status_button.geometry()

        # Set up the button's animation for changing its size
        self.button_anim.setEasingCurve(QEasingCurve.Type.InOutSine)
        self.button_anim.setDuration(1000)
        self.button_anim.setStartValue(start_geometry)
        self.button_anim.setKeyValueAt(0.5, QRect(QPoint(
            start_geometry.x() - 4, start_geometry.y() - 4),
            QSize(start_geometry.width() + 8, start_geometry.height() + 8)))
        self.button_anim.setEndValue(start_geometry)

        # Untoggle the check box if it is toggled
        if self.update_cb.isChecked():
            self.update_cb.toggle()
        self.update_cb.setText("RED ALERT!")

        # Set up the check box's animation for changing its color
        self.cb_anim.setDuration(500)
        self.cb_anim.setLoopCount(-1)
        self.cb_anim.setStartValue(QColor(0, 0, 0))
        self.cb_anim.setEndValue(QColor(255, 0, 0))

        # Start the sequential sequence
        self.seq_group.addAnimation(self.button_anim)
        self.seq_group.addAnimation(self.cb_anim)
        self.seq_group.start()

        # Finally, disable the button
        self.status_button.setEnabled(False)

    def stopFlashing(self):
        """Stop animations when the check box is checked."""
        self.seq_group.stop()
        # Update widgets
        self.update_cb.setText("Normal")
        self.update_cb.setStyleSheet("color: rgb(0, 0, 0)")
        self.status_button.setEnabled(True)

    def closeEvent(self, event):
        """Ensure that animations are stopped when closing
        the window to avoid errors."""
        running = QAbstractAnimation.State.Running
        if self.seq_group.state == running:
            self.seq_group.stop()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())