"""Listing 13-8
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys, argparse
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine

def parseCommandLine():
    """Use argparse to parse the command line for specifying
    a path to a QML file."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str,
        help="A path to a .qml file to be the source.",
        required=True)
    args = vars(parser.parse_args())
    return args

class MainView(QQmlApplicationEngine):

    def __init__(self):
        super().__init__()
        # Order matters here; need to check if the object was 
        # created before loading the QML file
        self.objectCreated.connect(self.checkIfObjectsCreated, 
            Qt.ConnectionType.QueuedConnection)
        self.load(QUrl(args["file"]))

    def checkIfObjectsCreated(self, object, url):
        """Check if QML objects have loaded without errors. 
        Otherwise, exit the program."""
        if object is None:
            QGuiApplication.exit(1)

if __name__ == "__main__":
    args = parseCommandLine() # Return command line arguments
    app = QGuiApplication(sys.argv)
    engine = MainView()
    sys.exit(app.exec())