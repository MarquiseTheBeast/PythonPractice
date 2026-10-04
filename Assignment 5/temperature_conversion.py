''' This program converts a degree in Fahrenheit to Celsius degree, or Celsius degree to Fahrenheit degree. '''

#TODO: define Global Constants
# Global constant values of absolute zero 
FAHRENHEIT_ABSOLUTE_ZERO = -459.67 
CELSIUS_ABSOLUTE_ZERO = -273.15 

def main():
    # Get the temperature type
    temperature_type = get_temperature_type()

    # Get the temperature degree value
    temperature = get_temperature(temperature_type)

    # Display the temperature conversion based on type of temperature type
    display_conversion(temperature_type, temperature)

# TODO: complete this function which prompt user for the temperature type (C or F) until a valid input is received.
def get_temperature_type():
    # User enters the convsersion type of either Fahrenhiet or Celsius
    while (conversion_type := input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")) != 'F' and conversion_type != 'C':
        # If Fahrenheit or Celsius type input is 'f' or 'c', break out the loop as the letters will be used and changed to uppercase for return
        if conversion_type == 'f' or conversion_type == 'c':
            break
        else:
            print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

    # Return the conversion type. The lowercase letter of the conversion type, 'f' or 'c', will be changed to uppercase if used.
    return conversion_type.upper()

# TODO: complete this function which prompt user for the temperature until a valid value is received.
def get_temperature(temperature_type):
    # Check whether the temperature type is Fahrenheit or Celsius
    if temperature_type == 'F':
       # User will enter Fahrenheit temperature degree that is greater than absolute zero.
        while (temperature_value := float(input("Enter the Fahrenheit temperature you want to convert: "))) < FAHRENHEIT_ABSOLUTE_ZERO:
            print(f"Invalid temperature. Please enter a temperature above absolute zero ({FAHRENHEIT_ABSOLUTE_ZERO:.2f})")
    elif temperature_type == 'C':
        # User will enter Celsius temperature degree that is greater than Celsius absolute zero
        while (temperature_value := float(input("Enter the Celsius temperature you want to convert: "))) < CELSIUS_ABSOLUTE_ZERO:
            print(f"Invalid temperature. Please enter a temperature above absolute zero ({CELSIUS_ABSOLUTE_ZERO:.2f})")

    # Return the temperature value 
    return temperature_value

# TODO: complete this function which perform conversion based on the type
def display_conversion(temperature_type, temperature):
    # If Fahrenheit, convert to Celsius. If Celsius, convert to Fahrenheit.
    if temperature_type == 'F':
        # Convert Fahrenheit value to Celsius
        fahrenheit_to_celsius = (temperature - 32) / 1.8 
        # Print the Fahrenheit degree converted to Celsius
        print(f"The temperature in Celsius is: {fahrenheit_to_celsius:.2f}") 
    elif temperature_type == 'C':
        # Convert Celsius value to Fahrenheit
        celsius_to_fahrenheit = (temperature * 1.8) + 32
        # Print the Celsius degree converted to Fahrenheit
        print(f"The temperature in Fahrenheit is: {celsius_to_fahrenheit:.2f}") 

if __name__ == "__main__":
    main()