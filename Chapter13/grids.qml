/* Listing 13-6
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

import QtQuick

Rectangle {  
    width: 200; height: 200
    color: "grey"

    Grid {
        id: grid
        rows: 2; columns: 2
        anchors.centerIn: parent
        spacing: 6
        // Add custom components to Column
        ColorRect { }
        ColorRect { }
        ColorRect { radius: 20 }
        ColorRect { }
    }   
}