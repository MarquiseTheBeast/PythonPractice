''' This program converts a degree in Fahrenheit to a degree in Celsius, or the other way around. '''

# Constant values of absolute zero
FAHRENHEIT_ABSOLUTE_ZERO = -459.67
CELSIUS_ABSOLUTE_ZERO = -273.15

# User enters temperature
temperature = float(input("Enter the temperature you want to convert: "))

# User selects the type of temperature of either Fahrenhiet or Celsisu
conversion_type = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")

# Checks wheter the input conversion type is Fahrenheit or Celsius
if conversion_type == 'F' or conversion_type == 'f':
    if temperature >= FAHRENHEIT_ABSOLUTE_ZERO:
        # Convert Fahrenheit value to Celsius
        fahrenheit_to_celsius = (temperature - 32) / 1.8
        print(temperature, "degrees in Fahrenheit is", f'{fahrenheit_to_celsius:.2f}', "degrees in Celsius.")
    else:
        # Prints when temperature value is below Fahrenheit absolute zero
        print("Invalid: Temperature must be above Fahrenheit absolute zero.")
elif conversion_type == 'C' or conversion_type == 'c':
    if temperature >= CELSIUS_ABSOLUTE_ZERO:
        # Convert Celsius value to Fahrenheit
        celsius_to_fahrenheit = (temperature * 1.8) + 32
        print(temperature, "degrees in Celsius is", f'{celsius_to_fahrenheit:.2f}', "degrees in Fahrenheit.")
    else:
        # Prints when temperature value is below Celsius absolute zero
        print("Invalid: Temperature must be above Celsius absolute zero.")
else:
    print("Invalid: Must either input 'F' for Fahrenheit or 'C' or Celsius.")