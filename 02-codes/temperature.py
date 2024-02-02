import machine
import time

class Measurement:
    def __init__(self):
        self.adcpin = 4
        self.sensor = machine.ADC(self.adcpin)  # Ensure the ADC pin is correctly assigned

    def read_temperature(self):
        # Read the ADC value and calculate temperature
        adc_value = self.sensor.read_u16()
        volt = (3.3 / 65535) * adc_value
        temperature = 27 - (volt - 0.706) / 0.001721
        return round(temperature, 1)

    def start_measurement(self):
        while True:
            temperature = self.read_temperature()
            print(temperature)
            time.sleep(0.5)  # Wait for 5 seconds before the next read

measurement = Measurement()
measurement.start_measurement()  # Corrected method call
