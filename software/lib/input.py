from machine import Pin

class Button:
    A = 5 #pin 1
    B = 2 #pin 2

class Input:
    def on_button_pressed(self, button, button_func):
        button_pin = Pin(button, Pin.IN)
        button_pin.irq(trigger = Pin.IRQ_RISING, handler=button_func)

    def on_pin_pressed(self, pin, pin_func):
        pin_pin = Pin(pin, Pin.IN)
        pin_pin.irq(trigger = Pin.IRQ_RISING, handler=pin_func)