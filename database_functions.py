import sqlite3 as sq
import datetime

con = sq.connect("library.db")
cur = con.cursor()

def  create_table():
    cur.execute("create table if not exists books(accno text primary key, title text, subtitle text, author text, coauthors text, pages int, price real, category text )")
    cur.execute("create table if not exists members(membership_no text primary key, name text, address text, contact_no text, category text, start_date date, expiry_date date, closing_date date, fine real)")
    cur.execute("create table if not exists circulations (serial_number text primary key , membership_number text, start_date integer, return_date  integer)")
    con.commit()

def insert_book(book_data):
    try:
        cur.execute("insert into books values(?,?,?,?,?,?,?,?)",book_data)
        con.commit()
        print(f"Book inserted Succesfully")

    except sq.IntegrityError:
        print("Error: Book with same assession number already exist")
        con.rollback()

def search_book(accno):
    cur.execute("select * from books WHERE accno=?",(accno,))
    return cur.fetchone()

def delete_book(accno):
    cur.execute("delete from books WHERE accno=?",(accno,))
    con.commit()

def get_all_book():
    cur.execute("select * from books")
    return cur.fetchall()

def insert_member(member_data):
    try:
        cur.execute("insert into members values(?,?,?,?,?,?,?,?,?)",member_data)
        con.commit()
        print("Member insertd successfully")

    except sq.IntegrityError:
        print("Error: Member with same Membership number already exist")
        con.rollback()

def search_member(membership_no):
    cur.execute("select * from members where membership_no=?",(membership_no,))
    return cur.fetchone()

def delete_member(membership_no):
    cur.execute("delete from members where membership_no=?",(membership_no,))
    con.commit()

def get_all_members():
    cur.execute("select * from members")
    return cur.fetchall()

def update_member(membership_no,new_data):
    cur.execute("update members set membership_no=?, name=?, address=?, contact_no=?, category=?, start_date=?, expiry_date, closing_date=?, fine=? where membership_no=?",(*new_data,membership_no))
    con.commit()

def update_membership_expiry_date():
    today = datetime.date.today()
    cur.execute("update members set expiry_date = case"
                "when category = 'A' then ? + 365*4"
                "when category = 'B' tehn ? + 365*3"
                "when category = 'C' then ? + 365*2"
                "when category = 'M' then ? + 365*1"
                "end", (today,today,today,today))

    con.commit()

def update_closing_expiry_date():
    today = datetime.date.today()
    cur.execute("update members set closing_date=? where closing_date is null",(today,))
    con.commit()

def update_member_fine(membership_no, fine):
    cur.execute("update members set fine = ? where membership_no=? ",(fine,membership_no))
    con.commit()

def insert_circulation(circulation_data):
    try:
        cur.execute("insert into circulations values(?,?,?,?)", circulation_data)
        con.commit()
        print("Circulation record inserted successfully")

    except sq.IntegrityError:
        print("Error: Circulation record with the same serial number already exists")
        con.rollback()

def search_circulation(serial_number):
    cur.execute("select * from circulations where serial_number=?", (serial_number,))
    return cur.fetchone()

def delete_circulation(serial_number):
    cur.execute("delete from circulations where serial_number=?", (serial_number,))
    con.commit()

def get_all_circulations():
    cur.execute("select * from circulations")
    return cur.fetchall()

def update_circulation(serial_number, new_data):
    cur.execute("update circulations set membership_number=?, start_date=?, return_date=? where serial_number=?", (*new_data, serial_number))
    con.commit()

def issue_book(serial_number, membership_number):
    try:
        today = datetime.date.today()
        cur.execute("insert into circulations (serial_number, membership_number, start_date) values (?, ?, ?)",
                    (serial_number, membership_number, today))
        con.commit()
        print("Book issued successfully")

    except sq.IntegrityError:
        print("Error: Book with the same serial number is already issued or does not exist")
        con.rollback()

def return_book(serial_number):
    try:
        today = datetime.date.today()
        cur.execute("update circulations set return_date=? where serial_number=?", (today, serial_number))
        con.commit()
        print("Book returned successfully")

    except sq.IntegrityError:
        print("Error: Book with the same serial number is not issued or does not exist")
        con.rollback()

def get_books_issued_to_member(membership_number):
    cur.execute("select * from circulations where membership_number=? and return_date is null", (membership_number,))
    return cur.fetchall()

def search_circulation_by_book(accno):
    cur.execute("SELECT * FROM circulations WHERE serial_number=?", (accno,))
    circulation_record = cur.fetchone()
    return circulation_record
def is_book_eligible_to_issue(accno, membership_no):
    book = search_book(accno)
    member = search_member(membership_no)

    if book and member:
        if book[7] == 'issuable' and member[4] == 'A':
            return True
        elif book[7] == 'no issueable':
            return False
        else:
            return True
    else:
        return False

def is_book_available(accno):
    circulation = search_circulation_by_book(accno)

    if circulation:
        return False
    else:
        return True
