import database_functions as df
import datetime

def calculate_expiry_date(start_date, category):
    if category == "A":
        return start_date + datetime.timedelta(days = 365*4)
    if category == "B":
        return start_date + datetime.timedelta(days = 365*3)
    elif category == "C":
        return start_date + datetime.timedelta(days = 365*2)
    elif category == "M":
        return start_date + datetime.timedelta(days = 365*1)
    
def get_member_input():
    membership_no = input("Enter membership number: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    contact_no = input("Enter contact number: ")
    category = input("Enter (A,B,C,M) category: ")
    start_date = datetime.date.today()
    expiry_date = calculate_expiry_date(start_date, category)
    closing_date = None
    fine_paid = 0.0
    return membership_no, name, address, contact_no, category, start_date, expiry_date, closing_date, fine_paid

def print_member_info(member_data):
    print("Member information: ")
    print(f"Membership number: {member_data[0]}")
    print(f"Member name: {member_data[1]}")
    print(f"Member Address: {member_data[2]}")
    print(f"Member contact number: {member_data[3]}")
    print(f"Category: {member_data[4]}")
    print(f"Start Date: {member_data[5]}")
    expiry_date = member_data[6]
    print(f"Expiry Date: {expiry_date if expiry_date else 'Not set'}")
    closing_date = member_data[7]
    print(f"Closing Date: {closing_date if closing_date else 'Not set'}")
    print(f"Fine Paid: {member_data[8]}")

def add_member():
    member = get_member_input()
    df.insert_member(member)

def search_member():
    membership_no = input("Enter the membership number to search: ")
    member = df.search_member(membership_no)
    if member:
        print_member_info(member)
    else:
        print(f"Member with membership number {membership_no} does not exist")

def delete_member():
    membership_no = input("Enter the membership number to delete: ")
    member = df.search_member(membership_no)
    if member:
        df.delete_member(membership_no)
        print(f"Member with membership number {membership_no} delted successfully")
    else:
        print(f"Member with membership number {membership_no} does not exist")

def edit_member():
    membership_no = input("Enter the membership number of the member you want to edit: ")
    member = df.search_member(membership_no)
    if member: 
        print("Current member information: ")
        print_member_info(member)
        new_data = get_member_input()
        df.update_member(membership_no, new_data)
        print(f"Member information updated")
    else:
        print(f"Member with membership number {membership_no} does not exist")

def list_all_members():
    members = df.get_all_members()
    if members:
        for member in members:
                print_member_info(member)
    else:   
        print("No members in the library")

def update_membership_expiry_date():
    membership_no = input("Enter the membership number: ")
    category = input("Enter the Category(A,B,C,M): ")
    df.update_membership_expiry_date(membership_no, category)
    print(f"Expiry Date Updated")

def update_membership_closing_date():
    membership_no = input("Enter the membership number: ")
    today = datetime.date.today()
    df.update_membership_closing_date(membership_no,today)
    print(f"Membership with number {membership_no} closed successfully on {today}")




        


