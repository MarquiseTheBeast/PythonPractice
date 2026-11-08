import random

'''
# This game will create a dictionary object using the state name as the key and the capital as the value.
# It will create a loop to randomly select a state and prompt the user to respond with the capital of the selected state. 
# This program will count the valid and invalid responses. 
# After the user quits the game, it prints a summary of the game result.
'''

def main():
    # Total number of correct/incorrect responses to keep track of. 
    total_correct_responses = 0
    total_incorrect_responses = 0

    # Game will continue running until user quits.
    game_running = True
    while game_running is True:
        # Assign a random state name
        state_name_selection = random_state_selection()

        try:
            # User is prompted to enter capital name of state, or to quit the game by inputting '0'. 
            capital_name_input = input(f"What is the capital of {state_name_selection}? (or enter 0 to quit): ")
    
            if capital_name_input != '0':
                # Check to see if the input answer is correct.
                is_answer_correct = check_if_answer_is_correct(capital_name_input, state_name_selection)
                if is_answer_correct:
                    print("That is correct.")
                    total_correct_responses += 1
                else:
                    print("That is incorrect.")
                    total_incorrect_responses += 1
            else:
                # End the game and print the total number of correct/incorrect responses. 
                game_running = False
                correct_response_string = "correct responses" if total_correct_responses != 1 else "correct response"
                incorrect_response_string = "incorrect responses" if total_incorrect_responses != 1 else "incorrect response"
                print(f"You had {total_correct_responses} {correct_response_string} and {total_incorrect_responses} {incorrect_response_string}.")
        except:
            # This is printed when the capital input string is detected as empty.
            print("Error: Invaid input.")
                
# Selects a random state name from the dictionary to return.
def random_state_selection():
    # Get the state dictionary and assign.
    state_dict = get_state_dictionary()

    # Randomly select a state name from the dictionary keys.
    state_names = list(state_dict.keys())
    selected_state = random.choice(state_names)
    return selected_state

# Checks if the user's input answer is correct.
def check_if_answer_is_correct(capital_input, name_of_selected_state):
    # Get the state dictionary and assign.
    state_dict = get_state_dictionary()

    # Checks the answer and fixes any mistakes in the input string, if it contains any. 
    capital_input = fix_answer_string(capital_input)

    # Get the selected state's dictionary value (capital name). 
    correct_capital_name_from_dict = state_dict.get(name_of_selected_state)

    # Checks answer to determine whether the answer matches the correct capital name before returning.
    is_answer_correct = True if (capital_input == correct_capital_name_from_dict) else False
    return is_answer_correct

# This function fixes the user's answer string and returns it fixed.
def fix_answer_string(answer_string):
    # Split the words of the answer string into a list, which also removes all whitespaces in the string. 
    answer_words = answer_string.split()
    fixed_string = ''

    # Checks if there's more than one word in the list.
    # This is very useful if a state has a capital name with two or more words.
    if len(answer_words) > 1:
        # Loop through each word where the first letter is set to uppercase and the rest is set to lowercase.
        # Afterwards, assign word to fixed string variable with a single empty space added.
        for i in range(len(answer_words)):
            word = answer_words[i][0].upper() + answer_words[i][1:].lower()
            fixed_string += word + ' '

        # The answer string is updated by the fixed string, alongside removing the whitespace at the end.
        answer_string = fixed_string[0:(len(fixed_string)-1)]
    # Check to make sure the single word has its first letter uppercase and the rest of the letters lowercase.
    elif not answer_words[0][0].isupper() or not answer_words[0][1:].islower(): 
        fixed_string = answer_words[0][0].upper() + answer_words[0][1:].lower()
        answer_string = fixed_string

    return answer_string

# Dictionary object of the state names and their capitals.
def get_state_dictionary():
    # Dictionary object of state names as the keys and their capitals as the value.
    state_dict = {'Hawaii': 'Honolulu',
                  'Wyoming': 'Cheyenne',
                  'Illinois': 'Springfield',
                  'Alabama': 'Montgomery', 
                  'Arizona': 'Phoenix', 
                  'Georgia': 'Atlanta', 
                  'Idaho': 'Boise', 
                  'Kentucky': 'Frankfort',
                  'Michigan': 'Lansing',
                  'Maryland': 'Annapolis',
                  'California': 'Sacramento',
                  'Delaware': 'Dover',
                  'Washington': 'Olympia',
                  'Texas': 'Austin',
                  'Pennsylvania': 'Harrisburg',
                  'Utah': 'Salt Lake City',
                  'Louisiana': 'Baton Rouge',
                  'Minnesota': 'Saint Paul',
                  'Arkansas': 'Little Rock',
                  'New Mexico': 'Santa Fe'
                  }
    return state_dict

if __name__ == '__main__':
    main()