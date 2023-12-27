import database_functions as df  

def get_book_input():
    accno = input("Enter accession number: ")
    title = input("Enter book title: ")
    subtitle = input("Enter book subtitle: ")
    author = input("Enter author name: ")
    coauthors = input("Enter coauthors name/names: ")
    pages = int(input("Enter number of pages: "))
    price = float(input("Enter price: "))
    category = input("Enter Category(issuable/no issueable): ")
    return  accno,title,subtitle,author,coauthors,pages,price,category

def print_book_info(book):
    print("\nBook Information:")
    print(f"Accession number: {book[0]}")
    print(f"Book title: {book[1]}")
    print(f"Book subtitle: {book[2]}")
    print(f"Book author name: {book[3]}")
    print(f"Book coauthor name/names: {book[4]}")
    print(f"Pages: {book[5]}")
    print(f"Price: {book[6]}")
    print(f"Category: {book[7]}")

def add_book():
    book_data = get_book_input()
    df.insert_book(book_data)

def search_book():
    accno = input("Enter accession number to search: ")
    book = df.search_book(accno)
    if book: 
        print_book_info(book)
    else:
        print(f"Book with accession number {accno} does not exist")

def delete_book():
    accno = input("Enter accession number to delete: ")
    book = df.search_book(accno)
    if book:
        df.delete_book(accno)
        print(f"Book with accession number {accno} deleted successfully")
    else:
        print(f"Book with accession number {accno} does not exist")

def list_all_books():
    books = df.get_all_book()
    if books:
        for book in books:
            print_book_info(book)
    else:
        print("No books in the library")

def edit_book():
    accno = input("Enter accession number of the book you want to edit: ")
    book = df.search_book(accno)
    if book:
        print("Current book information: ")
        print_book_info(book)
        new_data = get_book_input()
        df.update_book(accno, new_data)
        print(f"Book information updated")
    else:
        print(f'Book with accession number {accno} does not exist')

