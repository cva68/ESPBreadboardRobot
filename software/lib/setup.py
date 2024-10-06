from basic import Basic
from input import Input
from led import Led
from motor_driver import MotorDriver

def setup():
    kitronik_motor_driver = MotorDriver()
    led = Led((7,6,5,4,3),(8,9,10,11,12))
    input = Input()
    basic = Basic(led)

    return kitronik_motor_driver, led, input, basic
