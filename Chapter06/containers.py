"""Listing 6-8 to Listing 6-11
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QRadioButton, QGroupBox, QLineEdit, QTabWidget, 
    QHBoxLayout, QVBoxLayout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Containers Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window.
        Set up tab bar and different tab widgets."""
        # Create tab bar and different page containers
        tab_bar = QTabWidget(self)
        self.prof_details_tab = QWidget()
        self.background_tab = QWidget()

        tab_bar.addTab(self.prof_details_tab, "Profile Details")
        tab_bar.addTab(self.background_tab, "Background")

        # Call methods to create the pages
        self.profileDetailsTab()
        self.backgroundTab()

        # Create the layout for main window
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(tab_bar)
        self.setLayout(main_h_box)

    def profileDetailsTab(self): 
        """Profile page allows the user to enter their name, 
        address, and select their gender."""
        # Set up labels and line edit widgets 
        name_label = QLabel("Name")
        name_edit = QLineEdit()

        address_label = QLabel("Address")
        address_edit = QLineEdit()
 
        # Create radio buttons and their layout manager
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("Female")

        gender_h_box = QHBoxLayout()
        gender_h_box.addWidget(male_rb)
        gender_h_box.addWidget(female_rb)

        # Create group box to contain radio buttons 
        gender_gb = QGroupBox("Gender")
        gender_gb.setLayout(gender_h_box)

        # Add all widgets to the profile details page layout
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(name_label)
        tab_v_box.addWidget(name_edit)
        tab_v_box.addStretch()
        tab_v_box.addWidget(address_label)
        tab_v_box.addWidget(address_edit)
        tab_v_box.addStretch()
        tab_v_box.addWidget(gender_gb)

        # Set layout for profile details tab 
        self.prof_details_tab.setLayout(tab_v_box)

    def backgroundTab(self):
        """Background page lets users select their education background."""
        # Layout for education_gb
        ed_v_box = QVBoxLayout()

        # Create and add radio buttons to ed_v_box
        education_list = ["High School Diploma", "Associate's Degree",
            "Bachelor's Degree", "Master's Degree", "Doctorate or Higher"]
        for ed in education_list:
            self.education_rb = QRadioButton(ed)
            ed_v_box.addWidget(self.education_rb)

        # Set up group box to hold radio buttons
        self.education_gb = QGroupBox("Highest Level of Education")
        self.education_gb.setLayout(ed_v_box)

        # Create and set for background tab
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(self.education_gb)

        # Set layout for background tab 
        self.background_tab.setLayout(tab_v_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())