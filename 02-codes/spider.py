from machine import Pin, I2C
import pca9685
import time

# Initialisation
i2c = I2C(0, sda=Pin(XX), scl=Pin(YY))

# Initialize the PCA9685 using the I2C interface
pwm_driver = pca9685.PCA9685(i2c)
pwm_driver.freq(60)

# Function to set the servo position
def set_servo(channel, angle):
    # Convert the angle to duty cycle and set it
    # The specific conversion might depend on your servos' specifications
    duty = int((angle / 180) * 4096)
    pwm_driver.set_pwm(channel, 0, duty)

# Movement Control
# Move Forward
def forwared():
    # LEFT
    # DOWN TO UP
    for angle in range (0, 45, 1):
        set_servo(1, angle)
        set_servo(9, angle)
        time.sleep(0.01)

    # LEFT TO RIGHT
    for angle in range (0, 45, 1):
        # DOWN-UP
        set_servo(2, angle)
        set_servo(10, angle)
        time.sleep(0.01)

    # UP TO DOWN
    for angle in range (45, 0, 1):
        set_servo(1, angle)
        set_servo(9, angle)
        time.sleep(0.01)

    # RIGHT
    # DOWN TO UP
    for angle in range (0, 45, 1):
        set_servo(4, angle)
        set_servo(12, angle)
        time.sleep(0.01)

    # LEFT TO RIGHT
    for angle in range (0, 45, 1):
        set_servo(3, angle)
        set_servo(11, angle)
        time.sleep(0.01)

    # UP TO DOWN
    for angle in range (45, 0, 1):
        set_servo(4, angle)
        set_servo(12, angle)
        time.sleep(0.01)

    # MIDDLE
    # DOWN TO UP
    for angle in range (0, 45, 1):
        set_servo(5, angle)
        set_servo(8, angle)
        time.sleep(0.01)

    # LEFT TO RIGHT
    for angle in range (0, 45, 1):
        set_servo(6, angle)
        set_servo(7, angle)
        time.sleep(0.01)

    # BODY FORWARD
    # RIGHT TO LEFT
    for angle in range (45, 0, 1):
        set_servo(2, angle)
        set_servo(10, angle)
        set_servo(3, angle)
        set_servo(11, angle)
        time.sleep(0.01)

    # RIGHT TO LEFT
    for angle in range (45, 0, 1):
        set_servo(5, angle)
        set_servo(8, angle)
        time.sleep(0.01)

def backward():
    # LEFT
    # DOWN TO UP
    for angle in range (45, 0, 1):
        set_servo(1, angle)
        set_servo(9, angle)
        time.sleep(0.01)

    # LEFT TO RIGHT
    for angle in range (45, 0, 1):
        # DOWN-UP
        set_servo(2, angle)
        set_servo(10, angle)
        time.sleep(0.01)

    # UP TO DOWN
    for angle in range (0, 45, 1):
        set_servo(1, angle)
        set_servo(9, angle)
        time.sleep(0.01)

    # RIGHT
    # DOWN TO UP
    for angle in range (45, 0, 1):
        set_servo(4, angle)
        set_servo(12, angle)
        time.sleep(0.01)

    # LEFT TO RIGHT
    for angle in range (45, 0, 1):
        set_servo(3, angle)
        set_servo(11, angle)
        time.sleep(0.01)

    # UP TO DOWN
    for angle in range (0, 45, 1):
        set_servo(4, angle)
        set_servo(12, angle)
        time.sleep(0.01)

    # MIDDLE
    # DOWN TO UP
    for angle in range (45, 0, 1):
        set_servo(5, angle)
        set_servo(8, angle)
        time.sleep(0.01)

    # LEFT TO RIGHT
    for angle in range (45, 0, 1):
        set_servo(6, angle)
        set_servo(7, angle)
        time.sleep(0.01)

    # BODY FORWARD
    # RIGHT TO LEFT
    for angle in range (0, 45, 1):
        set_servo(2, angle)
        set_servo(10, angle)
        set_servo(3, angle)
        set_servo(11, angle)
        time.sleep(0.01)

    # RIGHT TO LEFT
    for angle in range (0, 45, 1):
        set_servo(5, angle)
        set_servo(8, angle)
        time.sleep(0.01)

def left():
    # LEFT
    # DOWN TO UP
    for angle in range (0, 45, 1):
        set_servo(1, angle)
        set_servo(9, angle)
        time.sleep(0.01)

    # RIGHT TO LEFT
    for angle in range (0, -45, 1):
        set_servo(2, angle)
        set_servo(10, angle)

    # UP TO DOWN
    for angle in range (45, 0, 1):
        set_servo(1, angle)
        set_servo(9, angle)

    # RIGHT
    # DOWN TO UP
    for angle in range (0, 45, 1):
        set_servo(4, angle)
        set_servo(12, angle)

    # LEFT TO RIGHT
    for angle in range (0, 45, 1):
        set_servo(3, angle)
        set_servo(11, angle)

    # UP TO DOWN
    for angle in range (45, 0, 1):
        set_servo(4, angle)
        set_servo(12, angle)

    # MIDDLE
    # DOWN TO UP
    for angle in range (0, 45, 1):
        set_servo(5, angle)
        set_servo(8, angle)

    # RIGHT TO LEFT
    for angle in range (0, -45, 1):
        set_servo(6, angle)

    # RIGHT TO LEFT
    for angle in range (0, 45, 1):   
        set_servo(7, angle)

    # BODY LEFT
    for angle in range (45, 0, 1):
        set_servo(2, angle)
        set_servo(10, angle)

    for angle in range (45, 0, 1):
        set_servo(3, angle)
        set_servo(11, angle) 

def right():
    # LEFT
    # DOWN TO UP
    for angle in range (45, 0, 1):
        set_servo(1, angle)
        set_servo(9, angle)
        time.sleep(0.01)

    # RIGHT TO LEFT
    for angle in range (-45, 0, 1):
        set_servo(2, angle)
        set_servo(10, angle)

    # UP TO DOWN
    for angle in range (0, 45, 1):
        set_servo(1, angle)
        set_servo(9, angle)

    # RIGHT
    # DOWN TO UP
    for angle in range (45, 0, 1):
        set_servo(4, angle)
        set_servo(12, angle)

    # LEFT TO RIGHT
    for angle in range (45, 0, 1):
        set_servo(3, angle)
        set_servo(11, angle)

    # UP TO DOWN
    for angle in range (0, 45, 1):
        set_servo(4, angle)
        set_servo(12, angle)

    # MIDDLE
    # DOWN TO UP
    for angle in range (45, 0, 1):
        set_servo(5, angle)
        set_servo(8, angle)

    # RIGHT TO LEFT
    for angle in range (-45, 0, 1):
        set_servo(6, angle)

    # RIGHT TO LEFT
    for angle in range (45, 0, 1):   
        set_servo(7, angle)

    # BODY LEFT
    for angle in range (0, 45, 1):
        set_servo(2, angle)
        set_servo(10, angle)

    for angle in range (0, 45, 1):
        set_servo(3, angle)
        set_servo(11, angle) 


# Control loop
while True:
