# Library Book Issue System

def load_books():
    books = []

    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")
        books.append(data)

    file.close()
    return books


def save_books(books):

    file = open("books.txt", "w")

    for book in books:
        file.write(book[0] + "," + book[1] + "," + str(book[2]) + "\n")

    file.close()


# Requirement 1: Display all books
def display_books(books):

    print("\nBook Records")

    for book in books:
        print("ID:", book[0], "| Name:", book[1], "| Quantity:", book[2])


# Requirement 2: Search book using Book ID
def search_book(books):

    book_id = input("Enter Book ID: ")

    for book in books:

        if book[0] == book_id:
            print("\nBook Found")
            print("ID:", book[0])
            print("Name:", book[1])
            print("Quantity:", book[2])
            return

    print("Book Not Found")


# Requirement 3: Issue a book
def issue_book(books):

    book_id = input("Enter Book ID to Issue: ")

    for book in books:

        if book[0] == book_id:

            if int(book[2]) > 0:

                book[2] = str(int(book[2]) - 1)

                save_books(books)

                print("Book Issued Successfully")

            else:
                print("Book Not Available")

            return

    print("Book Not Found")


# Requirement 4: Return a book
def return_book(books):

    book_id = input("Enter Book ID to Return: ")

    for book in books:

        if book[0] == book_id:

            book[2] = str(int(book[2]) + 1)

            save_books(books)

            print("Book Returned Successfully")
            return

    print("Book Not Found")


# Requirement 5: Display unavailable books
def unavailable_books(books):

    print("\nUnavailable Books")

    found = False

    for book in books:

        if int(book[2]) == 0:
            print(book[0], "-", book[1])
            found = True

    if found == False:
        print("No Unavailable Books")


# Requirement 6: Display books requiring restocking
def restocking_books(books):

    print("\nBooks Requiring Restocking")

    found = False

    for book in books:

        if int(book[2]) < 2:
            print(book[0], "-", book[1], "- Copies:", book[2])
            found = True

    if found == False:
        print("No Books Need Restocking")


# Main Program

books = load_books()

while True:

    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_books(books)

    elif choice == 2:
        search_book(books)

    elif choice == 3:
        issue_book(books)

    elif choice == 4:
        return_book(books)

    elif choice == 5:
        unavailable_books(books)

    elif choice == 6:
        restocking_books(books)

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
