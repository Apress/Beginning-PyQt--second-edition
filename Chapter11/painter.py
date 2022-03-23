"""Listing 11-11 to Listing 11-22
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import os, sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
    QToolBar, QStatusBar, QToolTip, QColorDialog, QFileDialog)
from PyQt6.QtCore import Qt, QSize, QPoint, QRect
from PyQt6.QtGui import (QPainter, QPixmap, QPen, QColor, QIcon, 
    QFont, QAction)

# Creates widget to be drawn on
class Canvas(QLabel):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        width, height = parent.width(), parent.height()

        # Create a pixmap object that will act as the canvas
        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)

        # Keep track of the mouse for getting mouse coordinates
        self.mouse_track_label = QLabel()
        self.setMouseTracking(True)

        # Initialize variables
        self.antialiasing_status = False
        self.eraser_selected = False

        self.last_mouse_pos = QPoint()
        self.drawing = False
        self.pen_color = Qt.GlobalColor.black
        self.pen_width = 2

    def selectDrawingTool(self, tool):
        """Determine which tool in the toolbar has been 
        selected."""
        if tool == "pencil":
            self.eraser_selected = False
            self.pen_width = 2
        elif tool == "marker":
            self.eraser_selected = False
            self.pen_width = 8
        elif tool == "eraser":
            self.eraser_selected = True
        elif tool == "color":
            self.eraser_selected = False
            color = QColorDialog.getColor()
            if color.isValid():
                self.pen_color = color

    def mouseMoveEvent(self, event):
        """Handle mouse movements. Track the coordinates of the
        mouse in the window and display in the status bar."""
        mouse_pos = event.pos()
        if (event.buttons() and Qt.MouseButton.LeftButton) and self.drawing:
            self.drawOnCanvas(mouse_pos)

        self.mouse_track_label.setVisible(True)
        sb_text = f"""<p>Mouse Coordinates: ({mouse_pos.x()}, 
            {mouse_pos.y()})</p>"""
        self.mouse_track_label.setText(sb_text)
        self.parent.status_bar.addWidget(self.mouse_track_label)

    def drawOnCanvas(self, points):
        """Performs drawing on canvas."""
        painter = QPainter(self.pixmap)

        if self.antialiasing_status:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.eraser_selected == False:
            pen = QPen(QColor(self.pen_color), self.pen_width)
            painter.setPen(pen)
            painter.drawLine(self.last_mouse_pos, points)

            # Update the mouse's position for next movement
            self.last_mouse_pos = points
        elif self.eraser_selected == True:  
            # Use the eraser 
            eraser = QRect(points.x(), points.y(), 12, 12)
            painter.eraseRect(eraser)
        self.update()

    def newCanvas(self):
        """Clears the current canvas."""
        self.pixmap.fill(Qt.GlobalColor.white)
        self.update()

    def saveFile(self):
        """Save a .png image file of current pixmap area."""
        file_format = "png"
        default_name = os.path.curdir + "/untitled." + file_format
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", 
                    default_name, "PNG Format (*.png)")

        if file_name:
            self.pixmap.save(file_name, file_format)
    
    def mousePressEvent(self, event):
        """Handle when mouse is pressed."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_mouse_pos = event.pos()
            self.drawing = True

    def mouseReleaseEvent(self, event):
        """Handle when mouse is released.
        Check when eraser is no longer being used."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
        elif self.eraser_selected == True:
            self.eraser_selected = False

    def paintEvent(self, event):
        """Create QPainter object.
        This is to prevent the chance of the painting being lost
        if the user changes windows."""
        painter = QPainter(self)

        target_rect = QRect()
        target_rect = event.rect()
        painter.drawPixmap(target_rect, self.pixmap, target_rect)
        painter.end()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(900, 600)
        self.setWindowTitle("11.1 – Painter GUI")

        QToolTip.setFont(QFont("Helvetica", 12))

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.createToolbar()
        self.show()

    def setUpMainWindow(self):
        """Create the canvas object that inherits from QLabel."""
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.new_act = QAction("New Canvas")
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.triggered.connect(self.canvas.newCanvas)

        self.save_file_act = QAction("Save File")
        self.save_file_act.setShortcut("Ctrl+S")
        self.save_file_act.triggered.connect(self.canvas.saveFile)

        self.quit_act = QAction("Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        # Create actions for Tool menu
        self.anti_al_act = QAction("AntiAliasing", checkable=True)
        self.anti_al_act.triggered.connect(self.turnAntialiasingOn)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create File menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_act)
        file_menu.addAction(self.save_file_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        # Create Tools menu and add actions
        file_menu = self.menuBar().addMenu("Tools")
        file_menu.addAction(self.anti_al_act)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def createToolbar(self):
        """Create the application's toolbar that contains
        painting tools."""
        tool_bar = QToolBar("Painting Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        # Set orientation of toolbar to the left side
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, tool_bar)
        tool_bar.setMovable(False)

        # Create actions and tooltips and add them to the toolbar
        pencil_act = QAction(QIcon("icons/pencil.png"), "Pencil", tool_bar)
        pencil_act.setToolTip("This is the <b>Pencil</b>.")
        pencil_act.triggered.connect(lambda: self.canvas.selectDrawingTool("pencil"))

        marker_act = QAction(QIcon("icons/marker.png"), "Marker", tool_bar)
        marker_act.setToolTip("This is the <b>Marker</b>.")
        marker_act.triggered.connect(lambda: self.canvas.selectDrawingTool("marker"))

        eraser_act = QAction(QIcon("icons/eraser.png"), "Eraser", tool_bar)
        eraser_act.setToolTip("Use the <b>Eraser</b> to make it all disappear.")
        eraser_act.triggered.connect(lambda: self.canvas.selectDrawingTool("eraser"))

        color_act = QAction(QIcon("icons/colors.png"), "Colors", tool_bar)
        color_act.setToolTip("Choose a <b>Color</b> from the Color dialog.")
        color_act.triggered.connect(lambda: self.canvas.selectDrawingTool("color"))

        tool_bar.addAction(pencil_act)
        tool_bar.addAction(marker_act)
        tool_bar.addAction(eraser_act)
        tool_bar.addAction(color_act)

    def turnAntialiasingOn(self, state):
        """Turn anitaliasing on or off."""
        if state:
            self.canvas.antialiasing_status = True
        else:
            self.canvas.antialiasing_status = False

    def leaveEvent(self, event):
        """QEvent class that is called when mouse leaves 
        screen's space. Hide mouse coordinates in status 
        bar if mouse leaves the window."""
        self.canvas.mouse_track_label.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(
        Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)
    window = MainWindow()
    sys.exit(app.exec())