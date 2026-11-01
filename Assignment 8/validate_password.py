'''
This program asks the user to enter a password. It checks the password against the policy:
# Must be at least 8 characters long 
# Must contain at least one uppercase letter, one lowercase letter, and one digit 
# May only contain letters and digits (no spaces or symbols) 
'''

# Constant variable
PASSWORD_LENGTH = 8     # Max length of the password

def main():
    valid = False

    # Loop until password input is valid.
    while not valid:
        # User is prompted to enter a password.
        password_input = input("Enter a password: ")

        # Check to make sure the password is valid.
        is_password_valid = True if (check_password_length(password_input) and check_for_letters_and_digits(password_input) and check_for_spaces_or_symbols(password_input)) else False
        if is_password_valid:
            valid = True

        if not valid:
            print("Password is invalid.")
        else:
            print("Password is valid.")

# Checks if the password length is long enough.
def check_password_length(password):
    # Grab length of password
    password_length = len(password)

    if password_length < PASSWORD_LENGTH:
        print(f"Password must be at least {PASSWORD_LENGTH} characters long.")
        return False
    return True

# Checks to make sure the password contains at least one uppercase, one lowercase, and one digit.
def check_for_letters_and_digits(password):
    # Variables to count the number of uppercase letters, lowercase letters, and digits found in the password string.
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    # Using for loop to check each character in the string that is an uppercase, lowercase, or digit before adding it to its assigned count variable.
    for ch in password:
        if ch.isupper():
            uppercase_count += 1
        elif ch.islower():
            lowercase_count += 1
        elif ch.isdigit():
            digit_count += 1

    # If the password does contain at least one uppercase, one lowercase, and one digit, return true.
    if uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1:
        return True
    print("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
    return False

# Checks to make sure the password doesn't contain any spaces or symbols.
def check_for_spaces_or_symbols(password):
    # Using isalnum() to make sure the password string is alphanumeric (containing only alphabetic letters and digits), which is also useful for returning false when any space or symbol is detected in the password string. 
    if not password.isalnum():
        print("Password must not contain any spaces or symbols. Password must contain at least one uppercase letter, one lowercase letter, and one digit.")
        return False
    return True

if __name__ == '__main__':
    main()