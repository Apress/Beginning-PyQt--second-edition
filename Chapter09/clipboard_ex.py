"""Listing 9-1 to Listing 9-4
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, 
    QPushButton, QTextEdit, QDockWidget, QFrame, QVBoxLayout)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 300)
        self.setWindowTitle("Clipboard Example")

        self.setUpMainWindow()
        self.createClipboardDock()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.central_tedit = QTextEdit()
        self.setCentralWidget(self.central_tedit)

    def createClipboardDock(self):
        """Set up clipboard and dock widget to display 
        text from the clipboard."""
        self.clipboard_tedit = QTextEdit()
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.pasteText)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.clipboard_tedit)
        dock_v_box.addWidget(paste_button)

        # Set the main layout for the dock widget,
        # then set the main widget of the dock widget
        dock_frame = QFrame()
        dock_frame.setLayout(dock_v_box)

        # Create a dock widget
        clipboard_dock = QDockWidget()
        clipboard_dock.setWindowTitle("Display Clipboard Contents")
        clipboard_dock.setAllowedAreas(
            Qt.DockWidgetArea.TopDockWidgetArea)
        clipboard_dock.setWidget(dock_frame)

        # Set initial location of dock widget
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, 
            clipboard_dock)

        # Create instance of the clipboard
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.copyFromClipboard)

    def copyFromClipboard(self):
        """Get the contents of the system clipboard and 
        paste to the window that has focus."""
        mime_data = self.clipboard.mimeData()
        if mime_data.hasText():
            self.clipboard_tedit.setText(mime_data.text())
            self.clipboard_tedit.repaint()
    
    def pasteText(self):
        """Paste text from clipboard if button is clicked."""
        self.central_tedit.paste()
        self.central_tedit.repaint()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())