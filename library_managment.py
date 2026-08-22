class Book:
    def __init__(self,book_id,title,author,category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_issued = False


book1 =Book(101,"python programming","Rs Aggarwal","programming")
book2 =Book(102,"PyshologyMindseat","Osho","Pyshology")




class Member:
    def __init__(self, member_id,name,phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone


member1 =Member(21,"Ashish gupta",9765456789)




class Library:
    def __init__(self):
        self.books = []
        self.members = [] 


###  Ab Library ko book add karna sikhana hai. - iske liye Hume ek method banana hai:
##  yaha humne Library class ke ander ek or method (add_book) banaya hai.
    def add_book(self,book):
        self.books.append(book)


    def display_books(self):
        for book in self.books:

            if book.is_issued:
                status ="issued"

            else:
                status = "available"
            print("status:",status)

            


    def issue_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued == False:
                    book.is_issued = True

                else:
                    print("book is already issued")

                return
        print("book not found")


    def search_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(book_id)
                print(book.title)
                print(book.author)
                print(book.category)

                return
                print("book not found")



    def add_member(self,member):
        self.members.append(member)



    def display_members(self):
        for member in self.members:
            print("Name",member.name)
            print("phone",member.phone)
            print("Member_id",member.member_id)

            


library1 = Library()
library1.add_book(book1)
library1.add_book(book2)

library1.issue_book(101)
library1.display_books()
library1.search_book(102)
library1.add_member(member1)
library1.display_members()



##  ================================
##     LIBRARY MANAGEMENT SYSTEM
##  ================================

while True:
    print("1. Add book")
    print("2. Display book")
    print("3. search book")
    print("4. Issue book")
    print("5. Add member")
    print("6. Display member")
    print("7. Exit")


    choice = int(input("Enter your choice : "))

    library1 = Library()
    library1.add_book(book1)
    library1.add_book(book2)


    
    if choice ==1:
        book_id =int(input("Enter book id:"))
        title = input("Enter book title:")
        author =input("Enter book author:")
        category =input("Enter category:")

        book =Book(book_id,title,author,category)
        library1.add_book(book)


    elif choice ==2:
        library1.display_books()

    elif choice ==3:
        book_id = int(input("Enter book id: "))
        library1.search_book(book_id)

    elif choice ==4:
        book_id = int(input("Enter book id: "))
        library1.issue_book(book_id)

    elif choice ==5:
        member_id = int(input("Enter member id: "))
        name = input("Enter member name: ")
        phone = int(input("Enter member phone: "))

        member =Member(member_id,name,phone)
        library1.add_member(member)

    elif choice ==6:
        library1.display_members()

    elif choice ==7:
        print("Thank you for using Library Management System")
        break

    else:
        print("invalid choice")