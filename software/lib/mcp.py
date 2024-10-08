"""
MCP23017 Lightweight MicroPython Driver
GNU GPL V3 (C) Connor Varney
"""

class MCPController:
    def __init__(self, i2c, address: int):
        self.i2c = i2c
        self.address = address
        self.bank_0_gpio = 0
        self.bank_1_gpio = 0
        self.buffer = bytearray(1)

    def set_all_output(self):
        """ Configure all banks as outputs"""
        self.i2c.writeto_mem(self.address, 0x00, b'\x00')
        self.i2c.writeto_mem(self.address, 0x01, b'\x00')
        #i2c.writeto_mem(0x20, 0x01, b'\x00')

    # The below functions are seperate to avoid conditional logic, in an attempt to keep
    # things as fast as possible
    def set_bank0_pin(self, pin: int):
        """ Clear pin of bank 0 """
        self.bank_0_gpio |= (1<<pin)
        self.i2c.writeto_mem(self.address, 0x12, self.bank_0_gpio.to_bytes(1, 'big'))

    def clear_bank0_pin(self, pin: int):
        """ Set pin of bank 1 """
        self.bank_0_gpio &= ~(1<<pin)
        self.i2c.writeto_mem(self.address, 0x12, self.bank_0_gpio.to_bytes(1, 'big'))
    
    def set_bank1_pin(self, pin: int):
        """ Clear pin of bank 0 """
        self.bank_1_gpio |= (1<<pin)
        self.i2c.writeto_mem(self.address, 0x13, self.bank_1_gpio.to_bytes(1, 'big'))

    def clear_bank1_pin(self, pin: int):
        """ Set pin of bank 1 """
        self.bank_1_gpio &= ~(1<<pin)
        self.i2c.writeto_mem(self.address, 0x13, self.bank_1_gpio.to_bytes(1, 'big'))

    def set_bank_0(self):
        """ Set entire bank """
        self.bank_0_gpio = 0xFF
        self.i2c.writeto_mem(self.address, 0x12, b'\xFF')
    
    def clear_bank_0(self):
        """ Clear entire bank """
        self.bank_0_gpio = 0
        self.i2c.writeto_mem(self.address, 0x12, b'\x00')
    
    def set_bank_1(self):
        """ Set entire bank """
        self.bank_1_gpio = 0xFF
        self.i2c.writeto_mem(self.address, 0x13, b'\xFF')
    
    def clear_bank_1(self):
        """ Clear entire bank """
        self.bank_1_gpio = 0
        self.i2c.writeto_mem(self.address, 0x13, b'\x00')
