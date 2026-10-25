TEXT_FILE = 'text_file2.txt'

def main():
    months = []
    numbers = []
    with open(TEXT_FILE, 'r') as file:
        for i in file:
            mon, val = i.split(',')

            tuple = (mon, val)
            (current_month, current_value) = tuple
  
            months.append(mon)
            numbers.append(val)

            print("Month:", current_month)
            print("Value:", current_value)

if __name__ == '__main__':
    main()