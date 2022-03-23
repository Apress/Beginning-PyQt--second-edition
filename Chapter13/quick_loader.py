"""Listing 13-3
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, argparse
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQuick import QQuickView

def parseCommandLine():
    """Use argparse to parse the command line for specifying
    a path to a QML file."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str,
        help="A path to a .qml file to be the source.",
        required=True)
    args = vars(parser.parse_args())
    return args

class MainView(QQuickView):

    def __init__(self):
        """ Constructor for loading QML files """
        super().__init__()
        self.setSource(QUrl(args["file"]))
        # Get the Status enum's value and check for an error
        if self.status().name == "Error":
            sys.exit(1)
        else:
            self.show()

if __name__ == "__main__":
    args = parseCommandLine() # Return command line arguments
    app = QGuiApplication(sys.argv)
    view = MainView()
    sys.exit(app.exec())