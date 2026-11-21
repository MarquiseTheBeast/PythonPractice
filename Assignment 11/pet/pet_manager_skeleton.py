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
    pets = []

    while True:
        print_menu()
        print(len(pets))
        choice = input("Enter choice: ").strip()

        if choice == '1':
            dog_name = input("Enter dog's name: ")
            new_dog = Dog(dog_name)
            pets.append(new_dog)
            print("Dog added to list.\n")
        elif choice == '2':
            cat_name = input("Enter cat's name: ")
            new_cat = Cat(cat_name)
            pets.append(new_cat)
            print("Cat added to list.\n")
        elif choice == '3':
            bird_name = input("Enter bird's name: ")
            new_bird = Bird(bird_name)
            pets.append(new_bird)
            print("Bird added to list.\n")
        elif choice == '4':
            if len(pets) != 0:
                for pet in pets:
                    sound = pet.make_sound()
                    print(sound)
            else:
                print("List is empty. Please add at least one pet.\n")
        elif choice == '5':
            break
        else:
            print("Invalid input. Try again.\n")

       # TODO


if __name__ == "__main__":
    main()
