/* Listing 13-4
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

import QtQuick

Rectangle {
    id: root
    width: 80; height: 80
    color: "#1FC6DE" // Cyan-like color
    border.color: "#000000"
    border.width: 4
    radius: 5

    Text {
        text: root.color
        anchors.centerIn: root
    }

    // Click on Rectangle to change the color
    MouseArea {
        anchors.fill: parent
        onClicked: {
            color = '#' + (0x1000000 + Math.random() 
                * 0xffffff).toString(16).substr(1, 6);
            // Uncomment the following line for Listing 13-9
            //root.clicked()
        }
    }
}
