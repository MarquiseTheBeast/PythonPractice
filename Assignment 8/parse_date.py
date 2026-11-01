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
MAX_THIRTY_ONE_DAYS = 31    # List of months with 31 days: January, March, May, July, August, October, December
MAX_THIRTY_DAYS = 30    # List of months with 30 days: April, June, September, November
FEBRUARY_MAX_DAYS = 28  # Max days for February, 29 days if in leap years

def main():
    is_valid_date = False

    # Looping until date is valid.
    while not is_valid_date:
        try:
            # User is prompted to enter date.
            date_input = input("Enter a date in the format mm/dd/yyyy: ")
            
            # Make sure date input string is in valid format before proceeding.
            if is_valid_format(date_input):
                # Split the '/' in the date string.
                month, day, year = date_input.split('/')
                
                # Convert the month, day, and year value strings to integers.
                month = int(month)
                day = int(day)
                year = int(year)
                
                # Check to make sure date values are valid before printing full English name of the date
                if is_date_valid(month, day, year):
                    full_english_name(month, day, year)
                    is_valid_date = True
            else:
                print("Error: Date must be in mm/dd/yyyy format with slashes.")
        except ValueError:
            print("Error: Invalid input. Please try again. Date must be in mm/dd/yyyy format with slashes.")

# This function checks if the date string is in valid format.
def is_valid_format(date_string):
    # Finding the '/' in the date string, which the valid date format must contain two slashes.
    find = '/'
    count = 0
    
    # Finding the '/' in the date string by searching each character in the string
    for char in date_string:
        if find in char:
            count += 1

    # Check if the date string contained two slashes
    if count == 2:
        return True
    return False

# This function checks if the date is valid by making sure the month value is within range, and the day value is within range for that selected month.
# Year value is used for calculating the leap year for February to determine whether it's 28-29 days
def is_date_valid(month, day, year):
    # Check which month is selected in the date range and checking if the day is within range.
    if month == JANUARY or month == MARCH or month == MAY or month == JULY or month == AUGUST or month == OCTOBER or month == DECEMBER:
        if day < MIN_DAY or day > MAX_THIRTY_DAYS:
            print(f"Error: Day must be between {MIN_MONTH} and {MAX_THIRTY_ONE_DAYS} for that month.")
            return False
    elif month == APRIL or month == JUNE or month == SEPTEMPER or month == NOVEMBER:
        if day < MIN_DAY or day > MAX_THIRTY_ONE_DAYS:
            print(f"Error: Day must be between {MIN_MONTH} and {MAX_THIRTY_DAYS} for that month.")
            return False
    elif month == FEBRUARY:
        # Calculate if the year is a leap year. 
        is_leap_year = True if (year % 4 == 0) else False

        # Check if February is in a leap year and checking day value is within range of February.
        if is_leap_year:
            if day < MIN_DAY or day > (FEBRUARY_MAX_DAYS + 1):
                print(f"Error: Day must be between {MIN_MONTH} and {FEBRUARY_MAX_DAYS + 1} for that month.")
                return False
        else:
            if day < MIN_DAY or day > FEBRUARY_MAX_DAYS:
                print(f"Error: Day must be between {MIN_MONTH} and {FEBRUARY_MAX_DAYS} for that month.")
                return False
    else:
        print(f"Error: Month must be between {MIN_MONTH} and {MAX_MONTH}.")
        return False
    return True

# This function prints the full English name of the month.
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
