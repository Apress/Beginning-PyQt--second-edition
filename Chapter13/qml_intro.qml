/* Listing 13-1
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

// Import necessary modules
import QtQuick

Rectangle {
    id: rect
    width: 155; height: 80
    color: "skyblue"

    Text {
        text: "Small Component"
        x: 10; y: 30
        font.pixelSize: 16
        font.weight: Font.DemiBold
        color: "black"
    }
}