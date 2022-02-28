class Library:
    def __init__(self, list_of_books = []):
        self.books=list_of_books


    def show_books(self):
        for book in self.books:
            print(book)
        print("\n")

    def take_book(self):
            name=input("ENTER NAME OF BOOK")
            if name in self.books:
                print(f"{name} BOOK IN NOW YOUT")
                self.books.remove(name)
                print("NOW AVALABILE BOOKS ARE ")
                for books in self.books:
                    print(books)
            else:
                print("WE HAVE THAT BOOK, HERE YOU GO AND ENJOY")


    def return_book(self):
        book=input("ENTER THE NAME OF BOOK YOU WILL RETURN")
        if book in self.books:
            print ("THAT BOOK IS NOT OURS")
        else:
            self.books.append(book)
            print("THANK YOU FOR RETURNIG BOOOK")
            for book in self.books:
                print(f"{book}")



    def donate_book(self):
        book = input("WHAT IS BOOK THAT YOU WILL DONATE")
        self.books.append(book)
        print("THANK YOU FOR DONATING TO ARE LIRARY ")


if __name__== "__main__" :
    l=Library(["milos", "milan", "mladen"])

    print("""
                WELCOME TO OUR LIBRARY 
                ENTER YOR CHOICE:
                1. SHOW AVAILABLE BOOKS
                2. TAKE BOOK 
                3. RETRUN BOOK
                4. DONATE BOOK
                5. EXIT MENU
                """)


    while (True):
        try:
            usr_response = int (input ("  Enter your Choice" ))

            if usr_response == 1:
                l.show_books()

            elif usr_response == 2:
                l.take_book()


            elif usr_response == 3 :
                l.return_book()

            elif  usr_response == 4 :
                l.donate_book()

            elif usr_response == 5:
                print("thank you")
                exit()

            else:
                print("Invalid input")

        except Exception as e:
            pass









