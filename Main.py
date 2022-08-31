# importing external module to get acesss in this module
import Return
import BooksList
import DateTime
import Borrow
import sys

#function name library is created to use in other module
def Library():
    while(True):
        print(''' xxxxxxxxxxxxxxxxxxxxxxxxx Welcome to the Library.xxxxxxxxxxxxxxxxxxxxxxxxx
- Press 1: To Display the books available.
- Press 2: To Borrow books of your choice.
- Press 3: To Return books you borrowed.
- Press 4: To Exit from the E-Library.''')

        #try,except block for exception handeling
        try:
            n = int(input("Enter your choice: "))
            print()
            # conditional statements for making desicion inside the program
            if(n==1):
                BooksList.list()
                print("The available books are : \n")
                print("Book Name \t\t Author Name \t\t Quantity \t Price \n")
                file=open("BookStock.txt","r")
                for i in range(3):
                    print(BooksList.BookName[i]+"\t\t"+BooksList.AuthorName[i]+"\t\t"+BooksList.Quantity[i]+"\t\t"+"$"+BooksList.Price[i])
                print()
                file.close()
                
            elif(n==2):
                BooksList.list()
                Borrow.BorrowBook()
                
            elif(n==3):
                BooksList.list()
                Return.ReturnBook()
                
            elif(n==4):
                print("Thank you for using our library system")
                break
            
            else:
                print("Please enter a number of your choice from1-4")
        except ValueError:
            print("\nPlease input the valid number.")
#closing the function
Library()

