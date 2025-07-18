from inventory import Book, load_inventory, save_inventory


def add_book(inventory):
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    book = Book(title, author, price, stock)
    inventory.append(book)
    print("Book added successfully!")


def view_books(inventory):
    if not inventory:
        print("No books available.")
        return
    for book in inventory:
        print(f"\nTitle: {book.title}")
        print(f"Author: {book.author}")
        print(f"Price: ${book.price:.2f}")
        print(f"Stock: {book.stock}")


def search_books(inventory):
    keyword = input("Enter title or author to search: ").lower()
    results = [book for book in inventory if keyword in book.title.lower(
    ) or keyword in book.author.lower()]
    if results:
        for book in results:
            print(
                f"\nTitle: {book.title}, Author: {book.author}, Price: ${book.price}, Stock: {book.stock}")
    else:
        print("No books found.")


def main():
    inventory = load_inventory()

    while True:
        print("\n--- Bookstore Inventory System ---")
        print("1. Add Book")
        print("2. View Inventory")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book(inventory)
            save_inventory(inventory)
        elif choice == "2":
            view_books(inventory)
        elif choice == '3':
            search_books(inventory)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
