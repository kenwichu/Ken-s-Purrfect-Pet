pets_available = {
    "kittens": {"Fluffy": ["Feed your kitten 2-3 times a day.", "Provide plenty of toys for playtime."],
                "Whiskers": ["Keep your kitten's litter box clean.", "Schedule regular veterinary check-ups."],
                "Mittens": ["Brush your kitten's fur regularly.", "Ensure your kitten has access to fresh water."]},
    "puppies": {"Buddy": ["Take your puppy for regular walks.", "Start obedience training early."],
                "Max": ["Provide your puppy with chew toys.", "Socialize your puppy with other dogs."],
                "Charlie": ["Feed your puppy a balanced diet.", "Teach your puppy basic commands like sit and stay."]},
    "hamsters": {"Nibbles": ["Provide your hamster with a cage that has plenty of room to explore.", "Offer your hamster a variety of fruits and vegetables as treats."],
                "Cocoa": ["Line your hamster's cage with safe bedding material.", "Make sure your hamster has a wheel for exercise."],
                "Peanut": ["Handle your hamster gently to build trust.", "Keep your hamster's cage away from direct sunlight."]}
}

user_accounts = {}

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.type = pet_type

    def play(self):
        print(f"Your pet {self.name} feels happy when you pet it.<3")

def sign_up():
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_accounts[username] = {"password": password, "gems": 0, "pets": []}
        print("Sign up successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

def sign_in():
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in user_accounts and user_accounts[username]["password"] == password:
            print("Sign in successful!")
            return username
        else:
            print("Invalid username or password.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_available_pets():
    try:
        print("Available pets:")
        for pet_type, pets in pets_available.items():
            print(f"{pet_type.capitalize()}: {', '.join(pets)}")
    except Exception as e:
        print(f"An error occurred: {e}")

def adopt_pet(username):
    try:
        pet_type = input("Enter the type of pet you want to adopt: ").lower()
        while True:
            pet_name = input("Enter the name of the pet you want to adopt: ")
            if pet_name in pets_available.get(pet_type, []):
                pet = Pet(pet_name, pet_type)
                user_accounts[username]["pets"].append(pet)
                pets_available[pet_type].pop(pet_name) 
                user_accounts[username]["gems"] += 1
                print(f"Congratulations! You adopted {pet_name}. You now have {user_accounts[username]['gems']} gems.")
                signed_in_menu(username)
                break
            else:
                print("Pet not available. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def play_with_pet(username):
    try:
        if not user_accounts[username]["pets"]:
            print("You don't have any pets to play with!")
            return
        print("Your pets:")
        for idx, pet in enumerate(user_accounts[username]["pets"], 1):
            print(f"{idx}. {pet.name} ({pet.type.capitalize()})")
        choice = int(input("Choose a pet to play with: "))
        if 1 <= choice <= len(user_accounts[username]["pets"]):
            pet = user_accounts[username]["pets"][choice - 1]
            pet.play()
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_more_gems(username):
    try:
        user_accounts[username]["gems"] += 10
        print("You earned 10 gems!")
    except Exception as e:
        print(f"An error occurred: {e}")

def exit_program():
    print("Exiting program.")
    quit()

def main():
    try:
        print("Welcome to Pet Adoption System!")
        while True:
            print("\nMain Menu:")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Display Available Pets")
            print("4. Adopt a Pet")
            print("5. Get More Gems")
            print("6. Play with Pet")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                sign_up()
            elif choice == "2":
                username = sign_in()
                if username:
                    signed_in_menu(username)
            elif choice == "3":
                display_available_pets()
            elif choice == "4":
                username = input("Enter your username: ")
                adopt_pet(username)
            elif choice == "5":
                username = input("Enter your username: ")
                get_more_gems(username)
            elif choice == "6":
                username = input("Enter your username: ")
                play_with_pet(username)
            elif choice == "7":
                exit_program()
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def signed_in_menu(username):
    try:
        while True:
            print("\nSigned In Menu:")
            print("1. Display Available Pets")
            print("2. Adopt a Pet")
            print("3. Get More Gems")
            print("4. Play with Pet")
            print("5. Sign Out")
            choice = input("Enter your choice: ")

            if choice == "1":
                display_available_pets()
            elif choice == "2":
                adopt_pet(username)
            elif choice == "3":
                get_more_gems(username)
            elif choice == "4":
                play_with_pet(username)
            elif choice == "5":
                print("Signing out.")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
