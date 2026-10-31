''' This program asks the user to enter a date in the format mm/dd/yyyy and prints the full English name of the date. '''

# Constant month
MIN_MONTH = 1 
MAX_MONTH = 12
JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMPER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

# Constant day
MIN_DAY = 1
MAX_DAY = 31

# Leap year
LEAP_YEAR = 4

def main():
    # User is prompted to enter date 
    date_input = input("Enter a date in the format mm/dd/yyyy: ")
    
    # Make sure date input string is valid
    if is_string_valid(date_input):
        # Split the '/' in the string 
        month, day, year = date_input.split('/')
        
        # Convert the month, day, and year value strings into integers
        month = int(month)
        day = int(day)
        year = int(year)
        
        # Check to make sure date values are valid before printing full English name of the date
        if is_date_values_valid(month, day):
            full_english_name(month, day, year)
    else:
        print("Error: Date must be in mm/dd/yy format with slashes.")
        
# In the date, it contains two slashes which must be detected before confirmation
def is_string_valid(date_input):
    find = '/'
    count = 0
    
    # Finding the '/' in the date string by searching each word in the string
    for char in date_input:
        if find in char:
            count += 1
    
    # Check if the date string contained two slashes
    if count == 2:
        return True
    return False

def is_date_values_valid(mm, dd):
    # Check to make sure month value is within range
    if mm < MIN_MONTH or mm > MAX_MONTH:
        print(f"Error: Month must be between {MIN_MONTH} and {MAX_MONTH}.")
        return False
        
    # Check to make sure day value is within range
    if dd < MIN_DAY or dd > MAX_DAY:
        print(f"Error: Day must be between {MIN_DAY} and {MAX_DAY}.")
        return False
    return True

# This function prints the full English name of the month
def full_english_name(mm, dd, yyyy):
    if mm == JANUARY:
        print(f"January {dd}, {yyyy}")
    elif mm == FEBRUARY:
        print(f"February {dd}, {yyyy}")
    elif mm == MARCH:
        print(f"March {dd}, {yyyy}")
    elif mm == APRIL:
        print(f"April {dd}, {yyyy}")
    elif mm == MAY:
        print(f"May {dd}, {yyyy}")
    elif mm == JUNE:
        print(f"June {dd}, {yyyy}")
    elif mm == JULY:
        print(f"July {dd}, {yyyy}")
    elif mm == AUGUST:
        print(f"August {dd}, {yyyy}")
    elif mm == SEPTEMPER:
        print(f"September {dd}, {yyyy}")
    elif mm == OCTOBER:
        print(f"October {dd}, {yyyy}")
    elif mm == NOVEMBER:
        print(f"November {dd}, {yyyy}")
    elif mm == DECEMBER:
        print(f"December {dd}, {yyyy}")
    
if __name__ == '__main__':
    main()
