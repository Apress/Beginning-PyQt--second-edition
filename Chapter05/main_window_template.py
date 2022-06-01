"""Listing 5-1 to Listing 5-2
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
from cProfile import label
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,QVBoxLayout,QHBoxLayout, QWidget,QDockWidget,
                             QPushButton, QMessageBox, QLabel, QLineEdit, QTextEdit ,QDial)
from PyQt6.QtGui import QAction,QFont, QIcon, QPixmap, QPainter, QPen, QColor, QFontMetrics, QFontDatabase
from PyQt6.QtCore import QCoreApplication,Qt, QSize, QPoint, QPointF, QLine, QTimer, QPropertyAnimation, QAbstractAnimation,pyqtSignal
import matplotlib.pyplot as  plt

from analoggaugewidget import AnalogGaugeWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")
        self.createActions()
        self.createMenu()
        self.setUpMainWindow()
        self.statusBar().showMessage("Ready")
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        """Create the dock widgets."""
        self.createDockWidget()
        #create vertical layout for battery status
        self.createBattery()
    def createDockWidget(self):
        """Create the dock widgets."""
        dock = QDockWidget("Dock Widget", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas) # Allow docking in all areas
        self.connectbuton=QPushButton("Connect")
        self.connectbuton.setStatusTip("Connect to the server.")
        self.connectbuton.setMinimumSize(QSize(100,50))
        self.connectbuton.clicked.connect(self.connect)
        butonlabel = QLabel()
        butonlabel.setText(f"{self.connectbuton.text()}")
        butonlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        butonlabel.setFont(QFont("Arial", 20))


        labelport = QLabel("Port")
        labelport.setStyleSheet("color: green")
        labelport.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelport.setFont(QFont("Arial", 20))
        labelport.setMinimumSize(QSize(100,50))
        # labelport.setFixedHeight(50)
        # labelport.setFixedWidth(100)
        editport = QLineEdit()
        editport.setStyleSheet("color: green")
        editport.setAlignment(Qt.AlignmentFlag.AlignCenter)
        editport.setFont(QFont("Arial", 20))
        editport.setFixedHeight(50)
        editport.setFixedWidth(100)
        hlayout = QHBoxLayout() 
        hlayout.addWidget(self.connectbuton)
        hlayout.addWidget(butonlabel)
        hlayout.addWidget(labelport)
        hlayout.addWidget(editport)
        containerdock = QWidget()
        containerdock.setLayout(hlayout)
        dock.setWidget(containerdock)
        dock.setFixedWidth(500)
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, dock) # add dock widget  right of main window
    def connect(self):
        """Connect to the server."""
        QMessageBox.information(self, "Connected", "Connected to the server.")
        self.connectbuton.setText("Disconnect")
    def createBattery(self):
        
        vlaue = QVBoxLayout()
        labelpower = QLabel("Power")
        labelpower.setStyleSheet("color: red")
        labelpower.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelpower.setFont(QFont("Arial", 20))
        labelpower.setFixedHeight(50)
        labelvoltage = QLabel("Voltage")
        labelvoltage.setStyleSheet("color: red")
        labelvoltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelvoltage.setFont(QFont("Arial", 20))
        labelvoltage.setFixedHeight(50)
        labelcurrent = QLabel("Current")
        labelcurrent.setStyleSheet("color: red")
        labelcurrent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelcurrent.setFont(QFont("Arial", 20))
        labelcurrent.setFixedHeight(50)
        labelpower.setFixedWidth(100)
        labelvoltage.setFixedWidth(100)
        labelcurrent.setFixedWidth(100)
        labelSoC = QLabel("SoC")
        labelSoC.setStyleSheet("color: red")
        labelSoC.setAlignment(Qt.AlignmentFlag.AlignCenter)
        labelSoC.setFont(QFont("Arial", 20))
        labelSoC.setFixedHeight(50)
        labelSoC.setFixedWidth(100)
        vlaue.addWidget(labelpower)
        vlaue.addWidget(labelvoltage)
        vlaue.addWidget(labelcurrent)
        vlaue.addWidget(labelSoC)
        #create vertical layout for battery status
        vlaue2 = QVBoxLayout()
        editpower = QLineEdit()
        editpower.setStyleSheet("color: red")
        editpower.setAlignment(Qt.AlignmentFlag.AlignCenter)
        editpower.setFont(QFont("Arial", 20))
        editpower.setFixedHeight(50)
        editvoltage = QLineEdit()
        editvoltage.setStyleSheet("color: red")
        editvoltage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        editvoltage.setFont(QFont("Arial", 20))
        editvoltage.setFixedHeight(50)
        editcurrent = QLineEdit()
        editcurrent.setStyleSheet("color: red")
        editcurrent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        editcurrent.setFont(QFont("Arial", 20))
        editcurrent.setFixedHeight(50)
        editSoC = QLineEdit()
        editSoC.setStyleSheet("color: red")
        editSoC.setAlignment(Qt.AlignmentFlag.AlignCenter)
        editSoC.setFont(QFont("Arial", 20))
        editSoC.setFixedHeight(50)
        editSoC.setFixedWidth(100)
        vlaue2.addWidget(editpower)
        vlaue2.addWidget(editvoltage)
        vlaue2.addWidget(editcurrent)
        vlaue2.addWidget(editSoC)

        gaugewidgets=self.createGaugeVelocity()
        vlaue3 = QVBoxLayout()
        vlaue3.addWidget(gaugewidgets)
        #create vertical layout for battery status
        hlayout = QHBoxLayout()
        hlayout.addLayout(vlaue)
        hlayout.addLayout(vlaue2)
        hlayout.addLayout(vlaue3)
        
        self.widget = QWidget()
        self.widget.setLayout(hlayout)
        self.setCentralWidget(self.widget)



    def createGaugeVelocity(self):
        """Create the gauge widgets."""
        self.gaugeVelocity = AnalogGaugeWidget(self)
        self.gaugeVelocity.setNotchesVisible(True) # show notches on the dial 
        self.gaugeVelocity.setNotchTarget(10) # set the notch target to 10
        self.gaugeVelocity.setMinimum(0) # set the minimum value to 0
        self.gaugeVelocity.setMaximum(100) # set the maximum value to 100
        self.gaugeVelocity.setValue(0) # set the value to 0
        self.gaugeVelocity.setFixedSize(200, 200) # set the size of the dial
        self.gaugeVelocity.setStyleSheet("background-color: transparent; color: red") # set the color of the dial
        self.gaugeVelocity.setFont(QFont("Arial", 20)) # set the font of the dial
        self.gaugeVelocity.setWrapping(True) # set the dial to wrap around
        return self.gaugeVelocity


    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions 
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())