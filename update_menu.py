        
def Update(): #Function to change the details of a customer
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name")
                    i[1]=i[1].upper()
                ch=input("Change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile")
                ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email")
                    i[3]=i[3].upper()
                ch=input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address")
                    i[4]=i[4].upper()
                ch=input("Change city(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City")
                    i[5]=i[5].upper()
                ch=input("Change Country(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country")
                    i[6]=i[6].upper()
                ch=input("Change Balance(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance"))
                cmd="UPDATE BANK SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
        else:
            print("Record not found")
    except:
        print("No such table")
