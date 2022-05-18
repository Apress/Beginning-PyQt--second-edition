"""Listing 4-17 to Listing 4-22
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QPushButton, QDateEdit, QLineEdit, QTextEdit, QComboBox,
    QFormLayout, QHBoxLayout)
from PyQt6.QtCore import Qt, QRegularExpression, QDate
from PyQt6.QtGui import QFont, QRegularExpressionValidator

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Appointment Form")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.first_name_edit = QLineEdit() 
        self.first_name_edit.setPlaceholderText("First")
        self.first_name_edit.textEdited.connect(self.clearText)
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Last")
        self.last_name_edit.textEdited.connect(self.clearText)

        # Create horizontal layout for names
        name_h_box = QHBoxLayout() # Create a horizontal layout 
        name_h_box.addWidget(self.first_name_edit) # Add the first name edit
        name_h_box.addWidget(self.last_name_edit)  # Add the last name edit

        # Create additional widgets to be added in the window
        gender_combo = QComboBox() # Create a combobox like Dropdownlist
        gender_combo.addItems(["Male", "Female"])

        self.phone_edit = QLineEdit()
        self.phone_edit.setInputMask("(999) 999-9999;_")# create mask for input
        self.phone_edit.textEdited.connect(self.clearText) # 

        self.birthdate_edit = QDateEdit() # Create a date edit widget 
        self.birthdate_edit.setDisplayFormat("MM/dd/yyyy")   # Set the format for the date edit widget 
        self.birthdate_edit.setMaximumDate(QDate.currentDate())  # Set the maximum date to today's date
        self.birthdate_edit.setCalendarPopup(True) # Set the calendar pop-up to true .it will display a calendar when the user clicks on the date edit widget.
        self.birthdate_edit.setDate(QDate.currentDate()) # Set the date to today's date

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("<username>@<domain>.com")
        reg_opt = QRegularExpression() # Create a regular expression object 
        regex = QRegularExpression(
            "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            reg_opt.PatternOption.CaseInsensitiveOption) # Set the regular expression to be case insensitive  "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b" is meant to match the email format

        self.email_edit.setValidator(QRegularExpressionValidator(regex)) # Set the validator to the regular expression object
        self.email_edit.textEdited.connect(self.clearText) # Connect the textEdited signal to the clearText method

        extra_info_tedit = QTextEdit()
        
        self.feedback_label = QLabel("")

        submit_button = QPushButton("SUBMIT")
        submit_button.setMaximumWidth(140) # Set the width of the button to 140 pixels
        submit_button.clicked.connect(self.checkFormInformation) 

        # Create horizontal layout for last row of widgets
        submit_h_box = QHBoxLayout()
        submit_h_box.addWidget(self.feedback_label)
        submit_h_box.addWidget(submit_button)      

        # Organize widgets and layouts in QFormLayout
        main_form = QFormLayout()
        main_form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow) # Set the field growth policy to all non-fixed fields grow ,it will grow the form to fit the contents of the form layout
        main_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop) # Set the form alignment to center horizontally and align the form to the top  of the widget
        main_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft) #set the label alignment to left

        main_form.addRow(header_label) # Add the header label to the form layout ina row (widget)
        main_form.addRow("Name", name_h_box) # Add the name widgets to the form layout in a row (string, layout)
        main_form.addRow("Gender", gender_combo) # add name widgets to the form layout in a row (string, widget)
        main_form.addRow("Date of Birth", self.birthdate_edit) # add name widgets to the form layout in a row (string, widget)
        main_form.addRow("Phone", self.phone_edit) # add name widgets to the form layout in a row (string, widget)
        main_form.addRow("Email", self.email_edit) # add name widgets to the form layout in a row (string, widget)
        main_form.addRow(QLabel("Comments or Messages")) # add label to the form layout in a row (widget)
        main_form.addRow(extra_info_tedit) # add name widgets to the form layout in a row (widget)
        main_form.addRow(submit_h_box) # add layout to the form layout in a row (layout)

        # Set the layout for the main window
        self.setLayout(main_form)
    #  end of setUpMainWindow()

    #  Clear the text in the text edit widgets when the user starts typing
    def clearText(self, text):
        """Clear the text for the QLabel that provides feedback."""
        self.feedback_label.clear()

    #  Check the form information and display a message if the form is complete 
    def checkFormInformation(self):
        """Demonstrates a few cases for validating user input."""
        if self.first_name_edit.text() == "" or self.last_name_edit.text() == "":
            self.feedback_label.setText("[INFO] Missing names.")
        elif self.phone_edit.hasAcceptableInput() == False: # Check if the phone number is valid
            self.feedback_label.setText("[INFO] Phone number entered incorrectly.")
        elif self.email_edit.hasAcceptableInput() == False: # Check if the email is valid
            self.feedback_label.setText("[INFO] Email entered incorrectly.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())