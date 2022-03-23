/* Listing 13-7
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

// Import necessary modules
import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs

ApplicationWindow {
    title: "QtQuick Image Viewer"
    width: 800; height: 500
    visible: true

    // Create the menu bar and its actions
    menuBar: MenuBar {
        Menu {
            title: "&File"
            Action {
                text: "&Open"
                onTriggered: openImage()
            }
            MenuSeparator {}
            Action {
                text: "&Quit"
                onTriggered: Qt.quit()}
        }
    }

    // Define the signal for opening images
    signal openImage()

    // Define the slot for opening images
    onOpenImage: {
        fileDialog.open()
    }
    
    // Define a FileDialog for selecting local images
    FileDialog {
        id: fileDialog
        title: "Choose an image file"
        nameFilters: ["Image files (*.png *.jpg)"]
        onAccepted: {
            // Update displayed image
            image.source = fileDialog.selectedFile
        }
        onRejected: {
            fileDialog.close()
        }
    }
    
    /* Create a container Rectangle for the image 
    in order to add margins around the image’s edges */
    Rectangle {
        id: container
        anchors {
            fill: parent
            margins: 10
        }

        Image {
            id: image
            anchors.fill: container
            source: "images/open_image.png"
            fillMode: Image.PreserveAspectFit
        }
    }
}