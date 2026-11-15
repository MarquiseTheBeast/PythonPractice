from pet import Pet

def main():
    # Entering the pet's name, type of animal, and age.
    pet_name = input("Enter the name of the pet: ")
    pet_type = input("Enter the type of animal: ")
    pet_age = int(input("Enter the age of the pet: "))

    # Printing the pet's name, animal type, and age.
    print("\nHere is the data that you entered:")
    new_pet = Pet(pet_name, pet_type, pet_age)
    print(new_pet)

if __name__ == '__main__':
    main()