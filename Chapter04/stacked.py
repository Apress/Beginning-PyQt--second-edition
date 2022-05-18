"""Listing 4-23 to Listing 4-27
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QStackedWidget,
    QStackedLayout, QFormLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(300, 340)
        self.setWindowTitle("QStackedLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        # Create and connect the combo box to switch between pages
        page_combo = QComboBox()
        page_combo.addItems([ "Description", "Image",
            "Additional Info"])
        page_combo.activated.connect(self.switchPage) #connect the activated signal to the switchPage method when the user selects a different page item from drop down menu

        # Create the Image page (Page 1)
        profile_image = QLabel()
        pixmap = QPixmap("images/norwegian.jpg") #create a QPixmap object passing in the image file path
        profile_image.setPixmap(pixmap) #set the QLabel's pixmap to the QPixmap object
        profile_image.setScaledContents(True) # set the image to be scaled to fit the label




        # Create the Profile page (Page 2)
        pg2_form = QFormLayout() #create a form layout
        pg2_form.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow) #set the form layout to grow all non-fixed fields (i.e. the line edit widgets) when the form layout is resized
        pg2_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop) #set the form layout to be horizontally centered and aligned to the top
        pg2_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft) #set the label text to be aligned to the left

        pg2_form.addRow("Breed:", QLabel("Norwegian Forest cat"))
        pg2_form.addRow("Origin:", QLabel("Norway"))
        pg2_form.addRow(QLabel("Description:"))
        default_text = """Have a long, sturdy body, long legs 
            and a bushy tail. They are friendly, intelligent, 
            and generally good with people."""
        pg2_form.addRow(QTextEdit(default_text))

        pg2_container = QWidget() #create a widget to hold the form layout and set its layout to be the form layout
        pg2_container.setLayout(pg2_form)


        # Create the About page (Page 3)
        pg3_form = QFormLayout()
        pg3_form.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg3_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        pg3_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        pg3_form.addRow(QLabel("Enter your cat's info."))
        pg3_form.addRow("Name:", QLineEdit())
        pg3_form.addRow("Color:", QLineEdit())

        age_sb = QSpinBox()
        age_sb.setRange(0, 30)
        pg3_form.addRow("Age:", age_sb)

        weight_dsb = QDoubleSpinBox()
        weight_dsb.setRange(0.0, 30.0)
        pg3_form.addRow("Weight (kg):", weight_dsb)

        pg3_container = QWidget() #create a widget to hold the form layout and set its layout to be the form layout
        pg3_container.setLayout(pg3_form)

        """
        QStackedLayout is a layout that allows you to stack different widgets
        on top of each other. The widgets are stacked in the order they are added
        to the layout.
        """
        # Create the stacked layout and add pages
        self.stacked_layout = QStackedLayout()
        # importance of the order of the pages in the stacked layout is that the first page is the default page
        self.stacked_layout.addWidget(pg2_container) #add the profile page to the stacked layout
        self.stacked_layout.addWidget(profile_image) #add the image page to the stacked layout
        self.stacked_layout.addWidget(pg3_container) #add the about page to the stacked layout

        # Add widgets and the stacked layout to the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(page_combo)
        main_v_box.addLayout(self.stacked_layout)

        # Set the layout for the main window
        self.setLayout(main_v_box)

    def switchPage(self, index): #index is the index of the selected item in the combo box
        """Slot for switching between tabs."""
        self.stacked_layout.setCurrentIndex(index) #set the stacked layout to display the selected page

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())