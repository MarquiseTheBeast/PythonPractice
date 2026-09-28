''' This program prints out a number of asterisk (or star) symbols on each row and column. '''
# Constant Variable
MAX = 7
ASTERISK_SYMBOL = '*'
# This will be used to print out the number of asterisk (or star) symbols using the MAX constant as the starting value
asterisk_symbols_to_print = MAX
# Print the number of asterisk symbols on the column of each row.
for row in range(MAX):
    for col in range(asterisk_symbols_to_print):
        print(ASTERISK_SYMBOL, end='')
    # Decrease the max number of asterisk symbols to print by 1 before the next row
    asterisk_symbols_to_print -= 1
    print("")