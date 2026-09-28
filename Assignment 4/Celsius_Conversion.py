''' This program will convert Celsius value to Fahrenheit degree. ''' 

# Constant values 
CELSIUS_ABSOLUTE_ZERO = -273.15  

# Input Celsius degree value that will afterwards check if the value is negative or less than absolute zero
while (input_celsius_degree_value := float(input("Enter a Celsius degree: "))) < 0: 
    if (input_celsius_degree_value < CELSIUS_ABSOLUTE_ZERO):
        print("Invalid: Temperature value must cannot be negative and must be greater than absolute zero.")
        continue
    print("Invalid: Temperature value must be greater than absolute zero.")

# Print output showing two colusn for Celsius and Fahrenheit
print("Celsius\t\tFahrenheit")  
print("---------------------------")

# Print each Celsius degree to Fahrenheit degree from zero up to the input Celsius degree.
for i in range(int(input_celsius_degree_value + 1)):
    # Convert Celsius to Fahrenheit  
    celsius_to_fahrenheit = (i * 1.8) + 32

    # Prints out value of Celsius degree converted to Fahrenheit degree
    print(i, f"\t\t{celsius_to_fahrenheit:.1f}")