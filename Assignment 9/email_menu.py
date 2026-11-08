import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    # TODO - Load emails, then loop reading a choice and calling the
    #        matching function below until the user quits, saving after
    #        add/change/delete.

    # Load dictionary contents from file and store in dictionary variable. 
    emails = load_emails()
    print("size:", len(emails))

    # Program continues running until user exits. 
    program_running = True
    while program_running:
        selection = get_user_choice()

        # Selection based on user choice input.
        if selection == LOOK_UP:
            look_up(emails)
        elif selection == ADD:
            add(emails)
        elif selection == CHANGE:
            change(emails)
        elif selection == DELETE:
            delete(emails)
        elif selection == QUIT:
            # Once finished, save email dictionary to file.
            save_emails(emails)
            program_running = False

def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    # TODO - Unpickle FILENAME; return an empty dict if it doesn't exist
    #        or is empty.
    # Empty dictionary that will be used to store the dictionary contents from the file.
    contents = {}

    # Open file and unpickle the objects, storing all contents inside the dictionary. 
    with open(FILENAME, 'rb') as file:
        contents = pickle.load(file)

    return contents

def get_user_choice():
    """Display the menu and return a validated choice."""
    # TODO - Print the menu, read a choice, and keep re-prompting until
    #        it's a valid menu option.
    print("\nMenu\n"
        "-------------------------------------\n"
        "1. Look up an email address\n"
        "2. Add a new name and email address\n"
        "3. Change an existing email address\n"
        "4. Delete a name and email address\n"
        "5. Quit the program\n")

    # Looping until input selection is valid.
    choice = 0
    try:
        while (input_selection := int(input("Enter a choice: "))) < LOOK_UP or input_selection > QUIT:
            print("Invalid input. Selection choice must be either 1, 2, 3, 4, or 5.")
        choice = input_selection
    except ValueError:
        print("Error: Input selection must be an integer. Selection choice must be either 1, 2, 3, 4, or 5.")
    return choice

def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    # TODO - Implement this function.
    # User is prompted to enter name
    name_input = input("Enter name: ")
    
    # Checks to see if the name input exists in the dictionary.
    if name_input in emails:
        # Print out both the name and email address. 
        email_address = emails.get(name_input)
        print(f"Name: {name_input}\nEmail: {email_address}")
    else:
        print("The specified name was not found.")

def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    # TODO - Implement this function.
    # User is prompted to enter name.
    name_input = input("Enter name: ")

    # Checks to see if the name input exists in the dictionary.
    if name_input not in emails:
        # Entering the new address for the name before adding to dictionary.
        new_address = input(f"Enter the new address for {name_input}: ")
        emails[name_input] = new_address
        print("Name and address have been added.")
    else:
        print("Name already exists.")

def change(emails):
    """Update the address for an existing name."""
    # TODO - Implement this function.

    # User is prompted to enter name.
    name_input = input("Enter name: ")

    # Checks to see if the name input exists in the dictionary.
    if name_input in emails:
        # User is prompted to enter a new address for the existing name before updating.
        new_address = input(f"Enter new address for {name_input}: ")
        emails[name_input] = new_address
        print("Information updated.")
    else:
        print(f"The specified name was not found.")

def delete(emails):
    """Remove a name/address pair."""
    # TODO - Implement this function.
    # User is prompted to enter name
    name_input = input("Enter name: ")

    # Checks to see if the name input exists in the dictionary.
    if name_input in emails:
        # Remove name and address from dictionary. 
        del emails[name_input]
        print(f"Information deleted.")
    else:
        print(f"The specified name was not found.")

def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    # TODO - Implement this function.

    # Open file and pickle the dictionary contents to the file.
    with open(FILENAME, 'wb') as output_file:
        pickle.dump(emails, output_file)
        print("Information saved to file.")

if __name__ == '__main__':
    main()
