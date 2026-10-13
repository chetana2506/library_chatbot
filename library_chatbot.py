books = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "available": True
    },
    {
        "title": "The Jungle Book",
        "author": "Rudyard Kipling",
        "genre": "Adventure",
        "available": True
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False
    },
    {
        "title": "The Secret Garden",
        "author": "Frances Hodgson Burnett",
        "genre": "Classic",
        "available": True
    },
    {
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "genre": "Science",
        "available": True
    }
]


def show_books():
    print("\nBOOKS IN THE LIBRARY:\n")

    for book in books:
        status = "Available" if book["available"] else "Borrowed"

        print(
            book["title"],
            "-",
            book["author"],
            "-",
            book["genre"],
            "-",
            status
        )


def search_book(name):

    for book in books:

        if name.lower() in book["title"].lower():

            status = "Available" if book["available"] else "Borrowed"

            print("\nBook found!")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Genre:", book["genre"])
            print("Status:", status)

            return

    print("\nSorry, I couldn't find that book.")


def chatbot():

    print("=" * 50)
    print("SCHOOL LIBRARY CHATBOT")
    print("=" * 50)

    print("Hello! I can help you find books.")
    print("Type 'help' for commands.")
    print("Type 'exit' to quit.")

    while True:

        user = input("\nYou: ")

        user = user.lower()

        if user == "exit":
            print("Library Bot: Goodbye! Happy reading!")
            break

        elif user == "help":
            print("\nYou can ask:")
            print("- show books")
            print("- search Harry Potter")
            print("- search Hobbit")
            print("- search Jungle Book")
            print("- search Secret Garden")
            print("- search Brief History")
            print("- exit")

        elif user == "show books":
            show_books()

        elif user.startswith("search "):

            book_name = user.replace("search ", "")

            search_book(book_name)

        else:
            print("Library Bot: Sorry, I don't understand.")
            print("Type 'help' to see what I can do.")


chatbot()