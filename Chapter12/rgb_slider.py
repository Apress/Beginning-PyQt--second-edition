"""Listing 12-1 to Listing 12-11
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QSlider, QSpinBox, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QImage, QPixmap, QColor, qRgb, QFont
from PyQt6.QtCore import Qt

style_sheet = """
    QSlider:groove:horizontal{
        border: 1px solid #000000;
        background: white;
        height: 10 px;
        border-radius: 4px
    }

    QSlider#Red:sub-page:horizontal{
        background: qlineargradient(x1:1, y1:0, x2:0, y2:1,
            stop: 0 #FF4242, stop: 1 #1C1C1C);
        background: qlineargradient(x1:0, y1:1, x2:1, y2:1,
            stop: 0 #1C1C1C, stop: 1 #FF0000);
        border: 1px solid #4C4B4B;
        height: 10px;
        border-radius: 4px;
    }

    QSlider::add-page:horizontal {
        background: #FFFFFF;
        border: 1px solid #4C4B4B;
        height: 10px;
        border-radius: 4px;
    }

    QSlider::handle:horizontal {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop: 0 #EEEEEE, stop: 1 #CCCCCC);
        border: 1px solid #4C4B4B;
        width: 13px;
        margin-top: -3px;
        margin-bottom: -3px;
        border-radius: 4px;
    }

    QSlider::handle:horizontal:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop: 0 #FFFFFF, stop: 1 #DDDDDD);
        border: 1px solid #393838;
        border-radius: 4px;
    }  

    QSlider#Green:sub-page:horizontal{
        background: qlineargradient(x1:1, y1:0, x2:0, y2:1,
            stop: 0 #FF4242, stop: 1 #1C1C1C);
        background: qlineargradient(x1:0, y1:1, x2:1, y2:1,
            stop: 0 #1C1C1C, stop: 1 #00FF00);
        border: 1px solid #4C4B4B;
        height: 10px;
        border-radius: 4px;
    } 

    QSlider#Blue:sub-page:horizontal{
        background: qlineargradient(x1:1, y1:0, x2:0, y2:1,
            stop: 0 #FF4242, stop: 1 #1C1C1C);
        background: qlineargradient(x1:0, y1:1, x2:1, y2:1,
            stop: 0 #1C1C1C, stop: 1 #0000FF);
        border: 1px solid #4C4B4B;
        height: 10px;
        border-radius: 4px;
    } 
"""

class RGBSlider(QWidget):

    def __init__(self, _image=None, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self._image = _image
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(225, 300)
        self.setWindowTitle("12.1 - RGB Slider")

        # Store the current pixel value 
        self.current_val = QColor()

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        # Image that will display the current color set by
        # slider/spin_box values
        self.color_display = QImage(100, 100, QImage.Format.Format_RGBX64)
        self.color_display.fill(Qt.GlobalColor.black)

        self.cd_label = QLabel()
        self.cd_label.setPixmap(QPixmap.fromImage(self.color_display))
        self.cd_label.setScaledContents(True)

        # Create RGB sliders and spinboxes
        red_label = QLabel("Red")
        red_label.setFont(QFont("Helvetica", 14))
        self.red_slider = QSlider(Qt.Orientation.Horizontal)
        self.red_slider.setObjectName("Red")
        self.red_slider.setMaximum(255)

        self.red_spinbox = QSpinBox()
        self.red_spinbox.setMaximum(255)

        green_label = QLabel("Green")
        green_label.setFont(QFont("Helvetica", 14))
        self.green_slider = QSlider(Qt.Orientation.Horizontal)
        self.green_slider.setObjectName("Green")
        self.green_slider.setMaximum(255)

        self.green_spinbox = QSpinBox()
        self.green_spinbox.setMaximum(255)

        blue_label = QLabel("Blue")
        blue_label.setFont(QFont("Helvetica", 14))
        self.blue_slider = QSlider(Qt.Orientation.Horizontal)
        self.blue_slider.setObjectName("Blue")
        self.blue_slider.setMaximum(255)

        self.blue_spinbox = QSpinBox()
        self.blue_spinbox.setMaximum(255)

        # Use the hex labels to display color values in hex format
        hex_label = QLabel("Hex Color ")
        self.hex_values_label = QLabel()

        hex_h_box = QHBoxLayout()
        hex_h_box.addWidget(hex_label, Qt.AlignmentFlag.AlignRight)
        hex_h_box.addWidget(self.hex_values_label, Qt.AlignmentFlag.AlignRight)

        hex_container = QWidget()
        hex_container.setLayout(hex_h_box)

        # Create grid layout for sliders and spinboxes
        grid = QGridLayout()
        grid.addWidget(red_label, 0, 0, Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.red_slider, 1, 0)
        grid.addWidget(self.red_spinbox, 1, 1)
        grid.addWidget(green_label, 2, 0, Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.green_slider, 3, 0)
        grid.addWidget(self.green_spinbox, 3, 1)
        grid.addWidget(blue_label, 4, 0, Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.blue_slider, 5, 0)
        grid.addWidget(self.blue_spinbox, 5, 1)
        grid.addWidget(hex_container, 6, 0, 1, 0)

        # The sliders and spinboxes for each color should display the 
        # same values and be updated at the same time
        self.red_slider.valueChanged.connect(self.updateRedSpinBox)
        self.red_spinbox.valueChanged.connect(self.updateRedSlider)

        self.green_slider.valueChanged.connect(self.updateGreenSpinBox)
        self.green_spinbox.valueChanged.connect(self.updateGreenSlider)

        self.blue_slider.valueChanged.connect(self.updateBlueSpinBox)
        self.blue_spinbox.valueChanged.connect(self.updateBlueSlider)

        # Create container for rgb widgets
        rgb_widgets = QWidget()
        rgb_widgets.setLayout(grid)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.cd_label)
        main_v_box.addWidget(rgb_widgets)

        self.setLayout(main_v_box)

    # The following slots update the red, green and blue
    # sliders and spinboxes
    def updateRedSpinBox(self, value):
        self.red_spinbox.setValue(value)
        self.redValue(value)
        
    def updateRedSlider(self, value):
        self.red_slider.setValue(value)
        self.redValue(value)

    def updateGreenSpinBox(self, value):
        self.green_spinbox.setValue(value)
        self.greenValue(value)
        
    def updateGreenSlider(self, value):
        self.green_slider.setValue(value)
        self.greenValue(value)

    def updateBlueSpinBox(self, value):
        self.blue_spinbox.setValue(value)
        self.blueValue(value)
        
    def updateBlueSlider(self, value):
        self.blue_slider.setValue(value)
        self.blueValue(value)

    # Create new colors based upon the changes to the RGB values
    def redValue(self, value):
        new_color = qRgb(value, self.current_val.green(), self.current_val.blue())
        self.updateColorInfo(new_color)

    def greenValue(self, value):
        new_color = qRgb(self.current_val.red(), value, self.current_val.blue())
        self.updateColorInfo(new_color)

    def blueValue(self, value):
        new_color = qRgb(self.current_val.red(), self.current_val.green(), value)
        self.updateColorInfo(new_color)

    def updateColorInfo(self, color):
        """Update color displayed in image and set the hex 
        values accordingly."""
        self.current_val = QColor(color)
        self.color_display.fill(color)

        self.cd_label.setPixmap(QPixmap.fromImage(
            self.color_display))
        self.hex_values_label.setText(f"{self.current_val.name()}")

    def getPixelValues(self, event):
        """The method reimplements the mousePressEvent method. 
        To use, set an widget's mousePressEvent equal to 
        getPixelValues, like so:
            image_label.mousePressEvent = rgbslider.getPixelValues
        If an _image != None, then the user can select pixels 
        in the images, and update the sliders to get view the color, 
        and get the rgb and hex values."""
        x = int(event.position().x())
        y = int(event.position().y()) 

        # valid() returns true if the point selected is a valid 
        # coordinate pair within the image
        if self._image.valid(x, y):
            self.current_val = QColor(self._image.pixel(x, y))

            red_val = self.current_val.red()
            green_val = self.current_val.green()
            blue_val = self.current_val.blue()

            self.updateRedSpinBox(red_val)
            self.updateRedSlider(red_val)
            self.updateGreenSpinBox(green_val)
            self.updateGreenSlider(green_val)
            self.updateBlueSpinBox(blue_val)
            self.updateBlueSlider(blue_val)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = RGBSlider()
    sys.exit(app.exec())