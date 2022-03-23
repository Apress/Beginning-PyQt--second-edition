/* Listing 13-5
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

import QtQuick

Rectangle {
    width: 200; height: 300 
    color: "grey"

    Column {
        id: column
        anchors.centerIn: parent
        spacing: 6
        // Add custom components to Column
        ColorRect { }
        ColorRect { }
        ColorRect { color: "pink"}
    }   
}