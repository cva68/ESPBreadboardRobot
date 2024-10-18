"""
ESP32 Compatibility layer for Kitronic Motor Driver functions in Microsoft MakeCode.
Part of ESPBreadboardRobot.
Copyright 2024 C. Varney, A. Walker, K.J Jones 
Free software under a MIT-0 License (see LICENSE.txt or https://github.com/aws/mit-0)
"""

from machine import Pin, PWM

class MotorDriver:
    class MotorReferences:
        """ Makecode uses MotorDriver.Motor, which is defined in the super __init__ using this as a template """
        def __init__(self, left_pins: tuple, right_pins: tuple):
            self.MOTOR1 = (PWM(Pin(left_pins[0])), PWM(Pin(left_pins[1])))
            self.MOTOR2 = (PWM(Pin(right_pins[0])), PWM(Pin(right_pins[1])))

    class MotorDirection:
        """ Makecode uses MotorDriver.MotorDirection, which can be treated as an enum """
        FORWARD = 0
        REVERSE = 1

    def __init__(self, left_pins: tuple, right_pins: tuple):
        """ Initialise the PWM pins and define the motor references for MakeCode """
        self.Motors = self.MotorReferences(left_pins, right_pins)
        self.motor_off(self.Motors.MOTOR1)
        self.motor_off(self.Motors.MOTOR2)

    def motor_off(self, motor):
        """ Turns the specified motor off by setting the PWM to 0 """
        motor[0].duty(0)
        motor[1].duty(0)

    def motor_on(self, motor, direction, speed):
        """ Turns on the specified motor at a set speed """
        speed = self.convert_speed(speed)
        motor[direction].duty(speed)

    def convert_speed(self, speed):
        """ Takes a speed from 0 to 100, and converts it to a PWM value between 0 and 1023 """
        return int((speed/100)*1023)