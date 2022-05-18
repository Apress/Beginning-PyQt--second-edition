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

class MainWindow(QMainWindow): # Inherits from QMainWindow class for main window with menu bar, etc.

    def __init__(self):
        super().__init__()
        self.initializeUI() # initialize the dock main window

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Adding More Window Features")

        self.setUpMainWindow() # Create and arrange widgets in the main window
        self.createDockWidget()# Create the application's dock widget ,it will be added to the left side of the main window 
        self.createActions() # Create the application's menu actions,if you want to add a menu to the main window,you must create the actions first
        self.createMenu() # Create the application's menu bar 
        self.createToolBar() # Create the application's toolbar,
        self.show() # Show the main window

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        # Create and set the central widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit) # Set the central widget for the main window to the text edit widget

        # Create the status bar
        self.setStatusBar(QStatusBar()) # QStatusBar is a widget that is placed at the bottom of the main window. it is used to display messages to the user. 

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        # QIcon is a class that provides access to the application's icon. QAction is a class that provides an action in a menu or toolbar.
        self.quit_act = QAction(QIcon("images/exit.png"), "Quit") 
        self.quit_act.setShortcut("Ctrl+Q") # Set the keyboard shortcut for the action
        self.quit_act.setStatusTip("Quit program") # Set the status tip for the action,it displays text in the status bar when the mouse cursor is over the menu item
        self.quit_act.triggered.connect(self.close) # Connect the triggered signal to the close() method

        # Create actions for Edit menu
        self.edit_action=QAction(QIcon("images/edit.png"), "Edit", self)
        self.edit_action.setShortcut("Ctrl+E")
        self.edit_action.setStatusTip("Editing the text")

        # Create actions for View menu
        self.full_screen_act = QAction("Full Screen", checkable=True) # Set the action to be checkable (i.e. it can be checked or unchecked),it means that the action will be displayed as a checkable menu item.
        self.full_screen_act.setShortcut("F11") # Set the keyboard shortcut for the action
        self.full_screen_act.setStatusTip("Switch to full screen mode") # Set the status tip for the action
        self.full_screen_act.triggered.connect(self.switchToFullScreen) # set trigger for the action,when the action is triggered,the method will be called

    def createMenu(self):
        """Create the application's menu bar."""
        menu_bar=self.menuBar()# create a menu bar
        menu_bar.setNativeMenuBar(False) # Set the menu bar to use native style (i.e. no OS-specific styling)
        # Create File menu and add actions 
        file_menu = menu_bar.addMenu("File") # Add a menu to the menu bar
        file_menu.addAction(self.quit_act) # Add an action to the menu

        # Create edit menu and add actions
        edit_menu = menu_bar.addMenu("Edit") # Add a menu to the menu bar

         # Create View menu, Appearance submenu and add actions 
        view_menu = menu_bar.addMenu("View")
        appearance_submenu = view_menu.addMenu("Appearance")
        appearance_submenu.addAction(self.full_screen_act)

        #Create Settings menu and add actions
        settings_menu = menu_bar.addMenu("Settings") # Add a menu to the menu bar

        #Create Run menu and add actions
        run_menu = menu_bar.addMenu("Run") # Add a menu to the menu bar

        #Create Terminals menu and add actions
        terminals_menu = menu_bar.addMenu("Terminals") # Add a menu to the menu bar

        #Create Help menu and add actions
        help_menu = menu_bar.addMenu("Help") # Add a menu to the menu bar



    def createToolBar(self):
        """Create the application's toolbar."""
        toolbar = QToolBar("Main Toolbar") # Create a toolbar with the name "Main Toolbar"
        toolbar.setIconSize(QSize(16, 16)) # Set the toolbar's icon size to 16x16 pixels
        toolbar.setMovable(False) # Set the toolbar to not be movable
        toolbar.setStatusTip("Main toolbar") # Set the status tip for the toolbar
        toolbar.setStyleSheet("QToolBar { border: 1px solid yellow; border-radius: 3px; background-color :  cyan }") # Set the toolbar's style sheet
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar) # Add the toolbar to the top of the main window


        # Add actions to the toolbar
        toolbar.addAction(self.quit_act)

    def createDockWidget(self):
        """Create the application's dock widget."""
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Format Tools") # Set the dock widget's title
        dock_widget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas) # Set the dock widget's allowed areas,it is used to specify where the dock widget can be docked.
        #set the dock widget's style sheet
        dock_widget.setStyleSheet("QDockWidget { border: 1px solid red; border-radius: 4px; background-color :  yellow }")
 
        # Create widget examples to add to the dock
        auto_bullet_cb = QCheckBox("Auto Bullet List") # Create a check box for the auto bullet list
        auto_bullet_cb.toggled.connect(self.changeTextEditSettings) # Connect the check box's toggled signal to the changeTextEditSettings() method

        # Create layout for dock widget
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(auto_bullet_cb) # Add the check box to the horizontal layout
        dock_v_box.addStretch(1) # Add a stretch to the layout ,1 is the stretch factor (0 is no stretch, 1 is maximum stretch),default is 0

        # Create a QWidget that acts as a container to 
        # hold other widgets
        dock_container = QWidget() # Create a widget to hold the layout
        dock_container.setLayout(dock_v_box) # Set the layout for the dock container

        # Set the main widget for the dock widget
        dock_widget.setWidget(dock_container) # Set the dock widget's main widget to the dock container

        # Set initial location of dock widget in main window
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget) # Change the text edit settings based on the check box state 

    def switchToFullScreen(self, state):
        """If state is True, then display the main window 
        in full screen. Otherwise, return the the window to normal."""
        if state: self.showFullScreen() # Show the main window in full screen
        else: self.showNormal() # Show the main window in normal mode

    def changeTextEditSettings(self, checked): # Change the text edit settings based on the check box state
        """Change formatting features for QTextEdit."""
        if checked:
            self.text_edit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoBulletList) # Set the text edit to automatically format lists when the user presses Enter,it is used to automatically insert bullets into a bulleted list when the user presses Enter.
        else:
            self.text_edit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoNone) # Set the text edit to not automatically format lists when the user presses Enter,it is used to automatically insert bullets into a bulleted list when the user presses Enter.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())