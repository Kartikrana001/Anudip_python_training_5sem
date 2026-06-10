# Mobile Contact Directory System

def load_contacts():

    contacts = []

    file = open("contacts.txt", "r")

    for line in file:
        data = line.strip().split(",")
        contacts.append(data)

    file.close()

    return contacts


def save_contacts(contacts):

    file = open("contacts.txt", "w")

    for contact in contacts:
        file.write(contact[0] + "," + contact[1] + "\n")

    file.close()


# Requirement 1: Display all contacts
def display_contacts(contacts):

    print("\nAll Contacts")

    for contact in contacts:
        print("Name:", contact[0], "| Number:", contact[1])


# Requirement 2: Search contact by name
def search_contact(contacts):

    name = input("Enter Name: ")

    for contact in contacts:

        if contact[0].lower() == name.lower():

            print("\nContact Found")
            print("Name:", contact[0])
            print("Number:", contact[1])

            return

    print("Contact Not Found")


# Requirement 3: Add a new contact
def add_contact(contacts):

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    contacts.append([name, number])

    save_contacts(contacts)

    print("Contact Added Successfully")


# Requirement 4: Update existing contact number
def update_contact(contacts):

    name = input("Enter Name to Update: ")

    for contact in contacts:

        if contact[0].lower() == name.lower():

            new_number = input("Enter New Number: ")

            contact[1] = new_number

            save_contacts(contacts)

            print("Contact Updated Successfully")

            return

    print("Contact Not Found")


# Requirement 5: Delete a contact
def delete_contact(contacts):

    name = input("Enter Name to Delete: ")

    for contact in contacts:

        if contact[0].lower() == name.lower():

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact Deleted Successfully")

            return

    print("Contact Not Found")


# Requirement 6: Display contacts starting with vowel
def vowel_contacts(contacts):

    print("\nContacts Starting With Vowel")

    found = False

    vowels = "AEIOUaeiou"

    for contact in contacts:

        if contact[0][0] in vowels:

            print(contact[0], "-", contact[1])

            found = True

    if found == False:
        print("No Contact Found")


# Main Program

contacts = load_contacts()

while True:

    print("\n===== Mobile Contact Directory System =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_contacts(contacts)

    elif choice == 2:
        search_contact(contacts)

    elif choice == 3:
        add_contact(contacts)

    elif choice == 4:
        update_contact(contacts)

    elif choice == 5:
        delete_contact(contacts)

    elif choice == 6:
        vowel_contacts(contacts)

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
