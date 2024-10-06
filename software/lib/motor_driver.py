from machine import Pin, PWM
from time import sleep

class Motors(Enum):
    MOTOR1 = 1 #right
    MOTOR2 = 2 #left

class MotorDirection(Enum):
    FORWARD = 1
    REVERSE = 2

class MotorDriver:
    def __init__(self):
        self.pwm_right_forward = PWM(Pin(2))  # PWM pin for the forward right motor
        self.pwm_right_reverse = PWM(Pin(10))  # PWM pin for the reverse right motor
        self.pwm_left_forward = PWM(Pin(6))   # PWM pin for the forward left motor
        self.pwm_left_reverse = PWM(Pin(7))   # PWM pin for the reverse left motor

        # Set initial duty cycle to 0
        self.pwm_right.duty(0)
        self.pwm_left.duty(0)

    def motor_off(self, motor):
        # Turns the specified motor off by setting the PWM to 0
        if motor == 1:
            self.pwm_right_forward.duty(0)
            self.pwm_right_reverse.duty(0)
        elif motor == 2:
            self.pwm_left_reverse.duty(0)
            self.pwm_left_reverse.duty(0)

    def motor_on(self, motor, direction, speed):
        if motor == 1:
            if direction = 1:
                self.pwm_right_forward.duty(speed)
            elif direction = 2:
                self.pwm_right_reverse.duty(speed)
        elif motor == 2:
            if direction = 1:
                self.pwm_left_forward.duty(speed)
            elif direction = 2:
                self.pwm_left_reverse.duty(speed)