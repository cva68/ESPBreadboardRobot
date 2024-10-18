"""
ESP32 Compatibility layer for pin / button interrupt functions in Microsoft MakeCode.
Part of ESPBreadboardRobot.
Copyright 2024 C. Varney, A. Walker, K.J Jones 
Free software under a MIT-0 License (see LICENSE.txt or https://github.com/aws/mit-0)
"""

from machine import Pin

class Button:
    """ Defines the pins used by each on-board button """
    A = 5 # Button A
    B = 2 # Button B

class Input:
    def on_button_pressed(self, button, button_func):
        button_pin = Pin(button, Pin.IN)
        button_pin.irq(trigger = Pin.IRQ_RISING, handler=button_func)

    def on_pin_pressed(self, pin, pin_func):
        pin_pin = Pin(pin, Pin.IN)
        pin_pin.irq(trigger = Pin.IRQ_RISING, handler=pin_func)