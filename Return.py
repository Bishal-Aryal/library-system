import BooksList
import DateTime
def ReturnBook():
    name=input("Enter name of borrower: ")
    a="Borrowed by-"+name+".txt"
    try:
        file=open(a,"r")
        lines=file.readlines()
        lines=[a.strip("$") for a in lines]
        file.close()
    
        file=open(a,"r")
        data=file.read()
        print(data)
    except:
        print("The borrower name is incorrect or not registered.")
        ReturnBook()

    Return="Returned by-"+name+".txt"
    file=open(Return,"w+")
    file.write("\t\t\tE-Library System\n")
    file.write("\n********************************************************************")
    file.write("\n\t\t Details of the returner and books returned\n")
    file.write("\t\t\t Returned By: "+ name+"\n")
    file.write("\t\t\t Date and Time: " + DateTime.getDateTime()+"\n\n")
    file.write("S.N. \t\t Book Name \t\t Price\n")
    file.close()
    count=0
    total=0.0
    for i in range(3):
        if BooksList.BookName[i] in data:
            count=count+1
            file=open(Return,"a")
            file.write(str(count)+" \t\t "+BooksList.BookName[i]+" \t\t"+" $"+BooksList.Price[i]+"\n")
            file.close()
            BooksList.Quantity[i]=int(BooksList.Quantity[i])+1
            total+=int(BooksList.Price[i])
            
    print("The book return date expires in 10 days. Has the book return date already expired?")
    print("Press Y for Yes and N for No")
    choice=input().upper
    if(choice()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=3*day
        file=open(Return,"a")
        file.write("\n\t\t\t\t\tfileine: $"+ str(fine)+"\n")
        file.close()
        total=total+fine
    

    print("Total: "+ "$"+str(total))
    file=open(Return,"a")
    file.write("\t\t\t\t\ Total: $"+ str(total))
    file.write("\n*************************************************************************************************************************")
    file.write("\nTHANK YOU fOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN")
    file.write("\n*************************************************************************************************************************")
    file.close()
    
        
    file=open("BookStock.txt","w+")
    for i in range(3):
        file.write(BooksList.BookName[i]+","+BooksList.AuthorName[i]+","+str(BooksList.Quantity[i])+","+"$"+BooksList.Price[i]+"\n")
    file.close()
