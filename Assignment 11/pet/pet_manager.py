# TODO: import your own Pet superclass and subclasses here, e.g.:
from dog import Dog
from cat import Cat
from bird import Bird

def print_menu():
    print("Pet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show All Pets")
    print("5. Exit")


def main():
    # List to store pets.
    pets = []

    while True:
        print_menu()

        # Entering number choice.
        choice = input("Enter choice: ").strip()

        if choice == '1':
            # Entering dog name.
            dog_name = input("Enter dog's name: ")

            # Create new dog class and add to list.
            new_dog = Dog(dog_name)
            pets.append(new_dog)
            print("Dog added to list.\n")
        elif choice == '2':
            # Entering cat name.
            cat_name = input("Enter cat's name: ")

            # Create new cat class and add to list.
            new_cat = Cat(cat_name)
            pets.append(new_cat)
            print("Cat added to list.\n")
        elif choice == '3':
            # Enter bird name.
            bird_name = input("Enter bird's name: ")

            # Create new bird class and add to list.
            new_bird = Bird(bird_name)
            pets.append(new_bird)
            print("Bird added to list.\n")
        elif choice == '4':
            # Check if list is empty before showing all pets.
            if len(pets) != 0:
                for pet in pets:
                    print(pet.make_sound())
                print()
            else:
                print("List is empty. Please add at least one pet.\n")
        elif choice == '5':
            break
        else:
            print("Invalid input. Try again.\n")

       # TODO


if __name__ == "__main__":
    main()
