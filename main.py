def on_pin_pressed_p0():
    pass
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_received_number(receivedNumber):
    radio.send_number(0)
    radio.send_string("")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_number(55)
    basic.show_leds("""
        . # # . .
        . # # . .
        . # # . .
        # # # # .
        # # # # .
        """)
    basic.show_string("Hello!")
    basic.clear_screen()
    basic.show_arrow(ArrowNames.NORTH)
    led.plot(0, 0)
    led.unplot(0, 0)
    led.toggle(0, 0)
    if input.button_is_pressed(Button.A):
        kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.FORWARD,
            0)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)
