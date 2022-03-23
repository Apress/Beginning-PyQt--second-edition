"""Listing 5-17 to Listing 5-22
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, 
    QWidget, QCheckBox, QTextEdit, QDockWidget, QToolBar, 
    QStatusBar, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Adding More Window Features")

        self.setUpMainWindow()
        self.createDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        # Create and set the central widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Create the status bar
        self.setStatusBar(QStatusBar())

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.quit_act = QAction(QIcon("images/exit.png"), "Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Quit program")
        self.quit_act.triggered.connect(self.close)

        # Create actions for View menu
        self.full_screen_act = QAction("Full Screen", checkable=True)
        self.full_screen_act.setStatusTip("Switch to full screen mode")
        self.full_screen_act.triggered.connect(self.switchToFullScreen)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create File menu and add actions 
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

        # Create View menu, Appearance submenu and add actions 
        view_menu = self.menuBar().addMenu("View")
        appearance_submenu = view_menu.addMenu("Appearance")
        appearance_submenu.addAction(self.full_screen_act)

    def createToolBar(self):
        """Create the application's toolbar."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Add actions to the toolbar
        toolbar.addAction(self.quit_act)

    def createDockWidget(self):
        """Create the application's dock widget."""
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Formatting")
        dock_widget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
 
        # Create widget examples to add to the dock
        auto_bullet_cb = QCheckBox("Auto Bullet List")
        auto_bullet_cb.toggled.connect(self.changeTextEditSettings)

        # Create layout for dock widget
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(auto_bullet_cb)
        dock_v_box.addStretch(1)

        # Create a QWidget that acts as a container to 
        # hold other widgets
        dock_container = QWidget()
        dock_container.setLayout(dock_v_box)

        # Set the main widget for the dock widget
        dock_widget.setWidget(dock_container)

        # Set initial location of dock widget in main window
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)

    def switchToFullScreen(self, state):
        """If state is True, then display the main window 
        in full screen. Otherwise, return the the window to normal."""
        if state: self.showFullScreen()
        else: self.showNormal()

    def changeTextEditSettings(self, checked):
        """Change formatting features for QTextEdit."""
        if checked:
            self.text_edit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoBulletList)
        else:
            self.text_edit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoNone)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())