import DateTime
import BooksList

def BorrowBook():
    Borrowed=False
    while(True):
        firstname=input("Input the first name of the borrower: ")
        if firstname.isalpha():
            break
        print("Please input alphabet only")
    while(True):
        lastname=input("Input the last name of the borrower: ")
        if lastname.isalpha():
            break
        print("Please input alphabet only")
            
    Borrow="Borrowed by-"+firstname+".txt"
    file=open(Borrow,"w+")
    file.write("\t\t\t E-Library System \n")
    file.write("\n*****************************************************************************")
    file.write("\n\t\t Details of the borrower and books borrowed\n")
    file.write("\t\t Borrowed By: "+ firstname+" "+lastname+"\n")
    file.write("\t\t Date and Time: " + DateTime.getDateTime()+"\n\n")
    file.write("S.N. \t\t Book Name \t\t\t Author Name \t\t Price\n" )
    file.close()

    total=0.0
    while Borrowed==False:
        print("\nPlease select a option below:\n")
        for i in range(3):
            print("Input",i, "to borrow book", BooksList.BookName[i])        
        try:   
            a=int(input())
            try:
                if(int(BooksList.Quantity[a])>0):
                    print("\nThe book you've selected is in stock.\n")
                    file=open(Borrow,"a")
                    file.write("1. \t\t"+ BooksList.BookName[a]+" \t\t\t "+BooksList.AuthorName[a]+" \t\t "+"$"+BooksList.Price[a]+"\n")
                    file.close()
                    BooksList.Quantity[a]=int(BooksList.Quantity[a])-1
                    total=total+int(BooksList.Price[a])
                    file=open("BookStock.txt","w+")
                    for i in range(3):
                        file.write(BooksList.BookName[i]+","+BooksList.AuthorName[i]+","+str(BooksList.Quantity[i])+","+"$"+BooksList.Price[i]+"\n")
                    file.close()
                    #multiple book borrowing code
                    Borrowed2=True
                    count=1
                    while Borrowed2==True:
                        choice=str(input("If you want to borrow another book then press Y for Yes if not then press N for No: \n").upper())
                        if(choice=="Y"):
                            count=count+1              
                            print("\nPlease select an option below:\n")
                            for i in range(3):
                                print("Input", i, "to borrow book", BooksList.BookName[i])
                            try:
                                b=int(input())
                                if b==a:
                                    print("I am sorry. You can't borrow the same book twice.")
                                    count=count-1
                                else:
                                    try:
                                        if(int(BooksList.Quantity[a])>0):
                                            print("\nThe book you've selected is in stock.\n")
                                            file=open(Borrow,"a")
                                            file.write(str(count)+". \t\t"+ BooksList.BookName[b]+"\t\t\t  "+BooksList.AuthorName[b]+" \t\t  "+"$"+BooksList.Price[b]+"\n")
                                            file.close()
                                            BooksList.Quantity[b]=int(BooksList.Quantity[b])-1
                                            total=total+int(BooksList.Price[b])
                                            file=open("BookStock.txt","w+")
                                            for i in range(3):
                                                file.write(BooksList.BookName[i]+","+BooksList.AuthorName[i]+","+str(BooksList.Quantity[i])+","+"$"+BooksList.Price[i]+"\n")
                                            file.close()
                                            Borrowed=False
                                        else:
                                            print("Book is not available right now. Please visit us after some time.")
                                            Borrowed2=False
                                            break
                                    except IndexError:
                                        print("\nPlease choose book acording to their number.")
                            except ValueError:
                                print("\nPlease input as suggested.")
                        elif(choice=="N"):
                            print("\nThank you for using our service to borrow books from us. ")
                            print("")
                            Borrowed2=False
                            Borrowed=True
                        else:
                            print("Please input as suggested")         
                else:
                    print("Book is not available right now. Please visit us after some time.")
                    Borrowed=False
                    
                file=open(Borrow,"a")
                file.write("\n\t\t\t\t\t\t\t\t\tTotal: $"+ str(total))
                file.write("\n*************************************************************************************************************************")
                file.write("\nTHANK YOU FOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN")
                file.write("\n*************************************************************************************************************************")
                file.close()
            except IndexError:
                print("\nPlease choose book acording to their number.")
        except ValueError:
            print("\nPlease input as suggested.")
