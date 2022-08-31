BookName=[]
AuthorName=[]
Quantity=[]
Price=[]
def list():
    file=open("BookStock.txt","r")
    lines=file.readlines()
    lines=[a.strip('\n') for a in lines]
    for i in range(len(lines)):
        x=0
        for j in lines[i].split(','):
            if(x==0):
                BookName.append(j)
            elif(x==1):
                AuthorName.append(j)
            elif(x==2):
                Quantity.append(j)
            elif(x==3):
                Price.append(j.strip("$"))
            x+=1
