def on_received_number(receivedNumber):
    global outdoorTemp
    outdoorTemp = 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

outdoorTemp = 0
radio.set_group(29)