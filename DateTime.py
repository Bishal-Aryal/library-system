#getting live time and date from system using inbuilt function 
def getDateTime():
    import datetime
    datetime=datetime.datetime.now()
    #print("Date and Time: ",datetime)
    return str(datetime)
