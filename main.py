import library_functions as lf 
import membership_funstions as mf 
import circulations_function as cf 
import database_functions as df

def main():
    df.create_table()
    print("\nChoose from the following menu: ")
    print(f"\na)Add book \tb)Search book \tc)Delete book \t"
          f"d)List all books \te)Edit books \tf)Quit the program \t"
          f"g)Add member \th)Search member \ti)Delete member \tj)Edit member "
          f"\tk)List all members \t"
          f"l)Update membership expiry \tm)Update membership closing "
          f"\tn)Add circulation\to)Search circulation\tp)Delete circulation\tq)List all members "
          f"\tr)Issue book\ts)Return book\t")
    menu_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
    choice = input("\nEnter any letter to execute to execute the function: ")
    while choice not in menu_list:
        print("\nChoose from the following menu: ")
        print(f"\na)Add book\tb)Search book\tc)Delete book\t"
          f"d)List all books\te)Edit books\tf)Quit the program\t"
          f"g)Add member\th)Search member\ti)Delete member\tj)Edit member"
          f"\tk)List all members\t"
          f"l)Update membership expiry\tm)Update membership closing"
          f"n)Add circulation\to)Search circulation\tp)Delete circulation\tq)List all members "
          f"\tr)Issue book\ts)Return book\t")
        choice = input("\nEnter any letter to execute to execute the function: ")

    if choice == "a":
        lf.add_book()
    elif choice == "b":
        lf.search_book()
    elif choice == "c":
        lf.delete_book()
    elif choice == "d":
        lf.list_all_books()
    elif choice == "e":
        lf.edit_book()
    elif choice == "f":
        print("Quitting the program")
        return
    elif choice == "g":
        mf.add_member()
    elif choice == "h":
        mf.search_member()
    elif choice == "i":
        mf.delete_member()
    elif choice == "j":
        mf.edit_member()
    elif choice == "k":
        mf.list_all_members()
    elif choice == "l":
        mf.update_membership_expiry_date()
    elif choice == "m":
        mf.update_membership_closing_date()
    elif choice == "n":
        cf.add_circulation()
    elif choice == "o":
        cf.search_circulation()
    elif choice == "p":
        cf.delete_circulation()
    elif choice == "q":
        cf.list_all_circulations()
    elif choice == "r":
        cf.issue_book()
    elif choice == "s":
        cf.return_book()
    

if __name__== "__main__":
    main()


    

