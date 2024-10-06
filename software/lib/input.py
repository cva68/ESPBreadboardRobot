from machine import Pin

class Button(Enum):
    A = 1 #pin 1
    B = 5 #pin 5

class Input:
    # def __init__(self):
    #     self.button_pressed = False

    def on_button_pressed(button, button_func):
        button_pin = Pin(button, Pin.IN)
        button.irq(trigger = Pin.IRQ_RISING, handler=handle_interrupt)

    def on_pin_pressed(pin, pin_func):
        pin = Pin(pin, Pin.IN)
        button.irq(trigger = Pin.IRQ_RISING, handler=handle_interrupt)
        pass