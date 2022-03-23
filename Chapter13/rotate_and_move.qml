/* Listing 13-9
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

import QtQuick
import QtQuick.Controls

ApplicationWindow {
    title: "Simple Transformations"
    width: 300; height: 300
    visible: true

    MouseArea {
        id: windowMouse
        anchors.fill: parent
        onClicked: {
            // Reset the values of the ColorRect objects
            rect1.rotation = 0
            rect2.scale = 1.0
        }
    }

    ColorRect { 
        id: rect1
        x: 20; y: 20 
        antialiasing: true
        signal clicked

        onClicked:{
            // Rotate the rect 20˚ when clicked
            rotation += 20
        }
    }
    ColorRect { 
        id: rect2;
        x: 200; y: 200
        antialiasing: true
        signal clicked

        onClicked:{
            // Scale the rect when clicked
            scale += .1
        }
    }
}