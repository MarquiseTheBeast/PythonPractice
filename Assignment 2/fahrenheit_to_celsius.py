''' This program converts a degree in Fahrenheit to a degree in Celsius. '''

# Prompt the user to input a temperature in Fahrenheit
fahrenheit = float(input("Please enter a degree in Fahrenheit: "))

# Convert Fahrenheit to Celsius
fahrenheit_to_celsius = (fahrenheit - 32) / 1.8

# Print the converted value.
print(fahrenheit, "degrees in Fahrenheit is", f'{fahrenheit_to_celsius:.2f}', "degrees in Celsius.")
