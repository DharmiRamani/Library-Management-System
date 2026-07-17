books = []
members = [] # admin ,user
issue_books = []
#---- Books ----
def add_book():   #-----add book details
    title = input("Enter Book Title : ").lower().strip()
    for t in books:
        if t["title"]==title:
            print("Book already exist.")
            return
    author = input("Enter Book Author : ").lower().strip()
    publisher = input("Enter Book  Publisher: ").lower().strip()
    book = {"title":title,"author":author,"publisher":publisher}
    books.append(book)
    print("Book add successfully.\n")
def remove_book():   #-----Delete book
    title = input("Enter Book title : ").lower().strip()
    for b in books:
        if b["title"] == title:
            books.remove(b)
            print("  Book removed successfully.\n")
            return
    print("Book not found\n.")
def search_book():  #-----search book
    title_author = input("Enter Book title or author name: ").lower().strip()
    found = False
    for b in books:
        if b["title"].find(title_author) != -1 or b["author"].find(title_author) != -1:             
            print(f"--> Title : {b['title']} | Author : {b['author']} | Publisher : {b['publisher']} \n")
            found = True
    if not found:
        print("Book not found.\n")
def update_book():   #-----Update Book
    update_title = input("Enter Book title for update details : ").lower().strip()
    for book in books:
        if book["title"] == update_title:
            book.update({"author":input("Enter Author : ").lower().strip(),
                         "publisher":input("Enter Publisher : ").lower().strip()})
            print("Update successfully.\n")
            return
    print("Book not found.\n")
def display_title():  #-----Display book title
    print(f"Total books : {len(books)}")
    for t in books:
        print("-",t['title'].title())
def display_books():   #-----Display Book all details
    for b in books:
        print(f"- Title : {b['title']} | Author : {b['author']} | Publisher : {b['publisher']} \n")
# ---- login / sign up ----
def sign_up():
    member_role = input("Enter role (admin / user) : ").lower().strip()
    if member_role!="admin" and member_role!="user":
        print("Invalid role\n")
        return
    
    member_name = input("Enter Member name : ").lower().strip() #---Member name
    for mname in members:
        if mname["member_name"] == member_name:
            print("Member name already exist.")
            return
    member_password = input("Enter Password : ").strip() #---Member password
    member_id = len(members) + 1  #---membere Id
        
    member = {"member_name":member_name,"member_password":member_password,"member_id":member_id,"member_role":member_role}
    members.append(member)
def login():
    role = input("Enter role (admin / user) : ").lower().strip()
    if role not in ["admin","user"]:
        print("Invalid role.\n")
        return None
    name = input("Enter name : ").lower().strip() 
    password = input("Enter Password : ").strip()

    for m in members:
        if m['member_name']==name and m['member_password']==password and m['member_role']==role:
            print(f"{role.title()} login successfully.\n")
            return role
    print("Invalid.\n")
    return

# ---- Members ----
def remove_member():   #-----Delete Member
    mname = input("Enter Member Name : ").lower().strip()
    for m in members:
        if m["member_name"] == mname:
            members.remove(m)
            print("  Member removed successfully.\n")
            return
    print("Member not exist\n.")
def search_member():  #-----search Member
    mname_mid = input("Enter Member Name / Id").lower().strip()
    found = False
    for m in members:
        if m["member_name"].find(mname_mid) != -1 or str(m["member_id"]).find(mname_mid) != -1:             
            print(f"--> Name : {m['member_name']} | Id : {m['member_id']} | Role : {m['member_role']}\n")
            found = True
    if not found:
        print("Member not exist.\n")
def update_member():   #-----Update Member
    ud_member = input("Enter Member Name for update details : ").lower().strip()
    for m in members:
        if m["member_name"] == ud_member:
            m.update({"member_name":input("Enter Member Name : ").lower().strip(),
                      "member_password":input("Enter Password : ").lower().strip()})
            print("Update successfully.\n")
            return
    print("Member not exist.\n")
def display_members():   #-----Display Members
    for m in members:
        print(f"- Name : {m['member_name']} | Id : {m['member_id']} \n")
#---- issue book ----
def issued_book():
    mname = input("Enter User Name : ").lower().strip()
    user_found = False
    for m in members:
        if m["member_name"] == mname and m["member_role"] == "user":
            user_found = True
            break
    if not user_found:
        print("User not found.\n")
        return
    
    title = input("Enter Book Title : ").lower().strip()
    book_in_library = False
    for b in books:
        if b["title"] == title:
            book_in_library = True
            break
    if not book_in_library:
        print("Book does not exist in library..\n")
        return
    for i in issue_books:
        if i["title"] == title:
            print("Book already issued.\n")
            return
            
    issue_books.append({"member" : mname,"title":title})
    print("Book issued successfully.\n")
#---- return Book ----
def return_book():
    mname = input("Enter User Name : ").lower().strip()
    title = input("Enter Book Title : ").lower().strip()

    for i in issue_books:
        if i["member"] == mname and i["title"] == title:
            issue_books.remove(i)
            print("Book returned succeefully.\n")
            return
    print("record not found.\n")
#---- Display Issued Book ----
def display_issued_book():
    if not issue_books:
        print("no books issued.\n")
        return
    for i in issue_books:
        print(f"User : {i['member']} | Book : {i['title']}")
# Main Menu
while True:
    print("--- Library Management System --- \n")
    print("1. Sign Up \n2. Login \n3. Exit")
    ch = int(input("Enter your choice(1-3) : "))
    print("--------------------------------")
    if ch == 1:
        sign_up()
    elif ch == 2:
        role = login()
        if role is None:
            continue # invalid login. main menu par pachhu jai
        elif role == "admin":
            while True:
                print("--- Admin Menu ---")
                print("1. Add Book \n2. Remove Book \n3. Search Book \n4. Update book \n5. Display Book title \n6. Display Books")
                print("7. Remove Member \n8. Search Member \n9. Update Member \n10. Display Member \n11. Display Issued Book \n12. Exit \n")
                choice = int(input("Enter your choice(1-12) : "))
                print("--------------------------------")
                if choice == 1:
                    add_book()
                elif choice == 2:
                    remove_book()
                elif choice == 3:
                    search_book()
                elif choice == 4:
                    update_book()
                elif choice == 5:
                    display_title()
                elif choice == 6:
                    display_books()
                elif choice == 7:
                    remove_member()
                elif choice == 8:
                    search_member()
                elif choice == 9:
                    update_member()
                elif choice == 10:
                    display_members()
                elif choice == 11:
                    display_issued_book()
                elif choice == 12:
                    print("Exiting Library system.")
                    break
                else:
                    print("Invalid Input.Try again \n")
        else:  
            while True:
                print("---- User Menu ----")
                print("1. Search User \n2. Update User \n3. Search Book \n4. Display Book title \n5. Display Books \n6. Issued Book \n7. return Book \n8.Exit \n")
                choice = int(input("Enter your choice(1-8) : "))
                print("--------------------------------")
                if choice == 1:
                    search_member()
                elif choice == 2:
                    update_member()
                elif choice == 3:
                    search_book()
                elif choice == 4:
                    display_title()
                elif choice == 5:
                    display_books()
                elif choice == 6:
                    issued_book()
                elif choice == 7:
                    return_book()
                elif choice == 8:
                    print("Exiting Library system.")
                    break
                else:
                    print("Invalid Input.Try again \n")
    elif ch == 3:
        print("Exiting Library system.")
        break
    else:
        print("Invalid Input.Try again \n")