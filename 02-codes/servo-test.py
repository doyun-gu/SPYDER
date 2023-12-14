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

# Example usage
servo0 = ServoDriver(0, 0)  # Channel 0 - GPIO 1

for angle in range(0, 90, 1):  # Test with a wider range and bigger steps
    print("Setting angle to:", angle)
    servo0.set_angle(angle)
    time.sleep(0.01)  # Increase delay to observe the movement

for angle in range(90, 0, -1):
    print("Setting back angle to:", angle)
    servo0.set_angle(angle)
    time.sleep(0.01)
