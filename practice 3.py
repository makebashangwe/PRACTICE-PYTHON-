import sys

phonebook = {}

def lookup_number(name):
    if name in phonebook:
        contact_name = phonebook.get(name)
        contact_number = phonebook.get(number)
        print(f"{contact_name}: {contact_number}")
    else:
        print("No contacts added.")

def add_contact(name,number):
    if name not in phonebook:
        phonebook[name] = name
        phonebook[number] = number
        print(f"Contact {name.capitalize().strip()} added.")
    else:
        print(f"Contact {name} already added.")

def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} @ {number} removed.")
    else:
        print(f"Contact {name} not found.")

open_book = True

while open_book == True:
    user_input = input("Welcome to the phone book.\n"
                       "1. Access Contacts\n"
                       "2. Add Contacts\n"
                       "3. Remove Contacts\n"
                       "4. See All Contacts\n"
                       "5. Exit Program\n"
                       "Please choose an action:")

    if user_input.isdigit():
        match user_input:
            case "1":
                name = input("Please enter the contact name: ")
                lookup_number(name)

            case "2":
                name = input("Please enter the contact name: ")
                number = input("Please enter the contact number: ")
                add_contact(name,number)

            case "3":
                name = input("Please enter the contact name: ")
                remove_contact(name)
            case "4":
                if len(phonebook)>0:
                    for i,(name,number) in enumerate(phonebook.items()):
                        print(f"{i+1}. Name: {name}: #{number}")
                else:
                    print("Squeaky Clean.")

            case "5":
                print("Thank you for using phonebook.")
                open_book = False
                sys.exit()
    else:
        print("Please enter a valid number.")

    again = input("Would you like to use the phonebook again? (y/n): ")
    if again.lower() == "y":
        open_book = True
    else:
        print("Thank you for using phonebook.")
        open_book = False
        sys.exit()