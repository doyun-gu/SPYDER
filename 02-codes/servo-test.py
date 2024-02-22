from machine import Pin, PWM
import time

class ServoDriver:
    def __init__(self, channel, pin_number):
        self.channel = channel
        self.pwm = PWM(Pin(pin_number))
        self.pwm.freq(50)  # Set frequency to 50 Hz

    def set_angle(self, angle):
        # Convert angle to duty cycle
        duty = self.angle_to_duty(angle)
        self.pwm.duty_u16(duty)

    @staticmethod
    def angle_to_duty(angle):
        # Map angle to duty cycle
        # 2^16 = 65535

        # 65535*(1 ms/20 ms) -- 20 ms is 50 Hz
        #min_duty = 1638  # Duty cycle for 0 degrees
        min_duty = 1000

        # 65535*(2 ms/20 ms) -- 20 ms is 50 Hz
        #max_duty = 8192  # Duty cycle for 180 degrees
        max_duty = 9000

        return int(min_duty + (max_duty - min_duty) * angle / 180)

"""
        ---usb---
GP0  1  |o     o| -1  VBUS
GP1  2  |o     o| -2  VSYS
GND  3  |o     o| -3  GND
GP2  4  |o     o| -4  3V3_EN
GP3  5  |o     o| -5  3V3(OUT)
GP4  6  |o     o| -6           ADC_VREF
GP5  7  |o     o| -7  GP28     ADC2
GND  8  |o     o| -8  GND      AGND
GP6  9  |o     o| -9  GP27     ADC1
GP7  10 |o     o| -10 GP26     ADC0
GP8  11 |o     o| -11 RUN
GP9  12 |o     o| -12 GP22
GND  13 |o     o| -13 GND
GP10 14 |o     o| -14 GP21
GP11 15 |o     o| -15 GP20
GP12 16 |o     o| -16 GP19
GP13 17 |o     o| -17 GP18
GND  18 |o     o| -18 GND
GP14 19 |o     o| -19 GP17
GP15 20 |o     o| -20 GP16
        ---------"""

# Example usage
servo0 = ServoDriver(0, 0)  # Channel 0 - GPIO 0

while 1:

    for angle in range(0, 90, 1):  # Test with a wider range and bigger steps
        print("Setting angle to:", angle)
        servo0.set_angle(angle)
        time.sleep(0.01)  # Increase delay to observe the movement
