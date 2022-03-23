"""Listing 6-1
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import QApplication, QStyleFactory

# Find out your OS's available styles
print(f"Keys: {QStyleFactory.keys()}")

# To find out the default style applied to an application
app = QApplication(sys.argv)
print(f"Default style: {app.style().name()}")