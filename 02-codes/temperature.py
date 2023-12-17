import machine
import time

# Initialize the temperature sensor
temp_sensor = machine.ADC(4) 

# Initialize the LED (replace 'LED_PIN' with your actual LED pin number)
led = machine.Pin("LED", machine.Pin.OUT)

def read_temperature():
    # Read raw value
    raw_value = temp_sensor.read_u16()
    # Convert to temperature (adjust this formula according to your sensor)
    temperature = 27 - (raw_value - 6731) / 184.33
    return temperature

# Function to check and print temperature only if it changes
def check_and_print_temperature(last_temp):
    current_temp = read_temperature()
    if current_temp != last_temp:
        print("Temperature:", current_temp, "C")
        led.on()  # Turn on LED when the temperature is printed
        time.sleep(0.5)  # Keep LED on for a short duration
        led.off()
    return current_temp

# Initialize last temperature
last_temperature = None

# Main loop
while True:
    last_temperature = check_and_print_temperature(last_temperature)
    time.sleep(1)
