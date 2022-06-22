def Insert():
    while True:     #Loop for accepting records
        Acc=input("Enter account no")
        Name=input("Enter Name")
        Mob=input("Enter Mobile")
        email=input("Enter Email")
        Add=input("Enter Address")
        City=input("Enter City")
        Country=input("Enter Country")
        Bal=float(input("Enter Balance"))
        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records")
        if ch=='N' or ch=='n':
            break
