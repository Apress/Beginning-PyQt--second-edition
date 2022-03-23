/* Listing 13-2
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

// Import necessary modules
import QtQuick

Item { 
    id: root
    width: 340; height: 420
    
    // Create an Image that will serve as the background 
    Image {
        anchors.fill: root
        source: "images/background.jpg"
        fillMode: Image.PreserveAspectCrop
    }

    // Create a container Rectangle to hold text and images
    Rectangle {
        id: container
        width: 300; height: 120
        y: 40 // Vertical offset
        /* Comment out the following line and uncomment the
        line after to view the Rectangle */
        color: "transparent"
        //color: "lightgrey" 

        anchors.horizontalCenter: root.horizontalCenter
        anchors.topMargin: 40

        Image {
            id: image
            anchors.centerIn: container
            source: "images/qtquick_text.png"
            sourceSize.width: container.width
            sourceSize.height: container.height
        }

        Text {
            text: "It's amazing!"
            anchors {
                top: image.bottom   
                horizontalCenter: image.horizontalCenter
            }
            font.pixelSize: 24
            font.weight: Font.DemiBold
            color: "#3F5674"
        }
    }
}
