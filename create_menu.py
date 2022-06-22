def Create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(20),BALANCE integer(15))')
        print("Table Created")
        Insert()
    except:
        print("Table Exist")
        Insert()
