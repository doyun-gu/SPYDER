
import machine
import time

class Measurement:
    def __init__(self):
        self.adcpin = 4
        self.sensor = machine.ADC(self.adcpin)  # Ensure the ADC pin is correctly assigned
        self.last_temperature = None  # Initialize last temperature

    def read_temperature(self):
        # Read the ADC value and calculate temperature
        adc_value = self.sensor.read_u16()
        volt = (3.3 / 65535) * adc_value
        temperature = 27 - (volt - 0.706) / 0.001721
        return round(temperature, 1)

    def update_measurement(self):
        while True:
            current_temperature = self.read_temperature()
            # Print every 5 seconds only if there's a change in temperature
            if self.last_temperature is None or current_temperature != self.last_temperature:
                variance = current_temperature - self.last_temperature if self.last_temperature is not None else 0
                print(f"Past Temperature: {self.last_temperature if self.last_temperature is not None else 'N/A'}")
                print(f"Current Temperature: {current_temperature}")
                print(f"Variance: {round(variance, 1)}")
                self.last_temperature = current_temperature
            time.sleep(5)  # Adjust to sleep for 5 seconds before the next read

measurement = Measurement()
measurement.update_measurement()
