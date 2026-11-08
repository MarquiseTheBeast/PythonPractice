from pathlib import Path

'''
# Read a text file and count the occurrences of each word referenced in this file.
# Use a dictionary object to store the word as the key and the count of occurrences as the value. 
# Do not contain duplicate keys. You can create a set object with a list as an argument to easily filter the duplicate word.
# This program is short and you can use main() to cover all instruction (no skeleton provided). Below is a sample output for your reference (partial).
'''
# Constant for path in the same folder. 
SAME_FOLDER = Path(__file__).resolve().parent

def main():
    # Input the file name.
    input_file_name = input("Enter the name of the input file: ")

    # Used to find the file in the same folder as the program. Will print an error if not found. 
    text_file = SAME_FOLDER / input_file_name

    try:
        # Dictionary to hold words as key words and values as count.
        words_dict = {}

        with open(text_file, 'r') as output:
            print("Word\t\tOccurrences")
            print("==============================================")

            # Reading each line in the text file.
            for line in output:
                # Removing the commas and periods from the string.
                words = line.replace(',', '').replace('.', '')
                words = words.split()

                # Loop for searching through each word in the list.
                for word in words:
                    # Check if word already exists in dictionary.
                    if word in words_dict:
                        # Add +1 to key's value every time the same word is found. 
                        words_dict[word] = words_dict.get(word) + 1
                    else:
                        # Create key and value.
                        words_dict[word] = 1

        # Set to store dictionary keys of the words.
        words_set = set(words_dict.keys())

        # Print each word and number of times word was found in text. .
        for i in words_set:
            print(f"{i:10}\t{words_dict[i]}")

    except FileNotFoundError:
        print(f"Error: {input_file_name} not found.")

if __name__ == '__main__':
    main()