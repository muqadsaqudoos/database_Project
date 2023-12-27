import database_functions as df
import datetime

def get_circulation_input():
    serial_number = input("Enter circulation serial number: ")
    membership_number = input("Enter membership number: ")
    start_date = datetime.date.today()
    return serial_number, membership_number, start_date, None  # None for return_date initially

def print_circulation_info(circulation_data):
    print("Circulation information:")
    print(f"Serial number: {circulation_data[0]}")
    print(f"Membership number: {circulation_data[1]}")
    print(f"Start date: {circulation_data[2]}")
    print(f"Return date: {circulation_data[3]}")

def add_circulation():
    circulation_data = get_circulation_input()
    df.insert_circulation(circulation_data)

def search_circulation():
    serial_number = input("Enter circulation serial number to search: ")
    circulation_data = df.search_circulation(serial_number)
    if circulation_data:
        print_circulation_info(circulation_data)
    else:
        print(f"Circulation record with serial number {serial_number} does not exist")

def delete_circulation():
    serial_number = input("Enter circulation serial number to delete: ")
    circulation_data = df.search_circulation(serial_number)
    if circulation_data:
        df.delete_circulation(serial_number)
        print(f"Circulation record with serial number {serial_number} deleted successfully")
    else:
        print(f"Circulation record with serial number {serial_number} does not exist")

def list_all_circulations():
    circulations = df.get_all_circulations()
    if circulations:
        for circulation in circulations:
            print_circulation_info(circulation)
    else:
        print("No circulation records in the library")

def issue_book():
    serial_number = input("Enter circulation serial number: ")
    accno = input("Enter accession number of the book: ")
    membership_no = input("Enter membership number: ")
    
    if df.is_book_eligible_to_issue(accno, membership_no) and df.is_book_available(accno):
        df.issue_book(serial_number, accno, membership_no)
        print(f"Book with serial number {serial_number} issued successfully")
    else:
        print(f"Cannot issue the book with serial number {serial_number}")

def return_book():
    serial_number = input("Enter circulation serial number: ")
    df.return_book(serial_number)
    print(f"Book with serial number {serial_number} returned successfully")
