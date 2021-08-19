from microbit import i2c


class Motor:
    # command
    LEFT = 0x21
    RIGHT = 0x20
    LEFT_INVERT = 0x13
    RIGHT_INVERT = 0x12
    ENABLE = 0x70

    # direction
    FORWARD = 0x80
    REVERSE = 0x00

    # i2c
    _I2C_ADDR = 0x59
    _I2C_SDA = 20
    _I2C_SCL = 19
    _i2c_buf = bytearray(2)

    def __init__(self, motor):
        self.motor = motor

    def set_speed(self, speed, direction=FORWARD):
        pwr = speed * 127 // 100
        Motor._i2c_buf[0] = self.motor
        Motor._i2c_buf[1] = (pwr | direction) \
                            if direction == Motor.FORWARD else (127 - pwr)
        i2c.write(Motor._I2C_ADDR, Motor._i2c_buf)

    def invert(self, invert):
        if self.motor == Motor.LEFT:
            Motor._i2c_buf[0] = Motor.LEFT_INVERT
        else:
            Motor._i2c_buf[0] = Motor.RIGHT_INVERT
        Motor._i2c_buf[1] = int(invert)
        i2c.write(Motor._I2C_ADDR, Motor._i2c_buf)

    @staticmethod
    def enable():
        Motor._i2c_buf[0] = Motor.ENABLE
        Motor._i2c_buf[1] = 1
        i2c.write(Motor._I2C_ADDR, Motor._i2c_buf)

    @staticmethod
    def disable():
        Motor._i2c_buf[0] = Motor.ENABLE
        Motor._i2c_buf[1] = 0
        i2c.write(Motor._I2C_ADDR, Motor._i2c_buf)


motor_left = Motor(Motor.LEFT)
motor_right = Motor(Motor.RIGHT)


if __name__ == '__main__':
    from microbit import button_a, sleep

    while True:
        if button_a.is_pressed():
            Motor.enable()
            motor_left.set_speed(100)
            motor_right.set_speed(100)
            sleep(1000)
            motor_left.set_speed(100, Motor.REVERSE)
            motor_right.set_speed(100)
            sleep(200)
            motor_left.set_speed(100)
            motor_right.set_speed(100)
            sleep(1000)
            Motor.disable()
