/* Listing 13-10
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
*/

import QtQuick
import QtQuick.Controls

ApplicationWindow {
    title: "Spin Wheel Transformations"   
    width: 500; height: 500
    visible: true 

    /* Get a random number where both the minimum and maximum
    values are inclusive */
    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1) + min);
    }

    Image {
        id: pointer
        source: "images/pointer.png"
        x: parent.width / 2 - width / 2; y: 0; z: 1
    }

    Image {
        id: spinwheel
        anchors.centerIn: parent
        source: "images/spin_wheel.png"
        sourceSize.width: parent.width - 30
        sourceSize.height: parent.height - 30

        // Create a behavior for rotating the spinwheel Image
        Behavior on rotation {
            NumberAnimation {
                duration: getRandomIntInclusive(500, 3000)
                easing.type: Easing.OutSine
            }
        }

        /* Enable mouse handling and define how the image rotates
        when clicked */
        MouseArea {
            anchors.fill: parent
            onClicked: spinwheel.rotation += getRandomIntInclusive(
                360, 360 * 4)
        }
    }
}