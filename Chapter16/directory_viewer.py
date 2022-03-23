"""Listing 16-1
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
    QTreeView, QFrame, QFileDialog, QVBoxLayout)
from PyQt6.QtGui import QFileSystemModel, QAction

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("16.1 – View Directory GUI")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        """Set up the QTreeView in the main window to 
        display the contents of the local filesystem."""
        self.model = QFileSystemModel()
        self.model.setRootPath("")

        self.tree = QTreeView()
        self.tree.setIndentation(10)
        self.tree.setModel(self.model)

        # Set up container and layout 
        frame = QFrame()
        frame_v_box = QVBoxLayout()
        frame_v_box.addWidget(self.tree)
        frame.setLayout(frame_v_box)

        self.setCentralWidget(frame)

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for Directories menu
        self.open_dir_act = QAction("Open Directory...")
        self.open_dir_act.triggered.connect(self.chooseDirectory)

        self.root_act = QAction("Return to Root")
        self.root_act.triggered.connect(self.returnToRootDirectory)

    def createMenu(self):
        """Create the application's menu bar.""" 
        self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions 
        dir_menu = self.menuBar().addMenu("Directories")
        dir_menu.addAction(self.open_dir_act)
        dir_menu.addAction(self.root_act)

    def chooseDirectory(self):
        """Slot for selecting a directory to display."""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        directory = file_dialog.getExistingDirectory(self, "Open Directory", 
                "", QFileDialog.Option.ShowDirsOnly)

        self.tree.setRootIndex(self.model.index(directory))

    def returnToRootDirectory(self):
        """Slot for redisplaying the contents of the root directory."""
        self.tree.setRootIndex(self.model.index(""))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())