radio.onReceivedNumber(function (receivedNumber) {
    outdoorTemp = 1
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
let outdoorTemp = 0
radio.setGroup(29)
