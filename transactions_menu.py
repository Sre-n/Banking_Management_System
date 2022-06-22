def Debit(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc=input("Enter the account no from which the money is to be debited")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("Enter the amount to be withdrawn"))
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("Amount Debited")
                    break
                else:
                    print("There must be min balance of Rs 5000")
                    break
        else:
            print("Record Not found")
    except:
        print("Table Doesn't exist")

        
def Credit(): #function to credit money into a account
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        acc=input("Enter the account no from which the money is to be debited")
        for i in S:
            i=list(i)
            if i[0]==acc:
                Amt=float(input("Enter the amount to be credited"))
                i[7]+=Amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Credited")
                break
        else:
            print("Record Not found")
    except:
        print("Table Doesn't exist")
while True:
    Menu()
    ch=input("Enter your Choice")
    if ch=="1":
        Create()
    elif ch=="2":
        while True:
            MenuSort()
            ch1=input("Enter choice a/b/c/d")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortName()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="3":
        DispSearchAcc()
    elif ch=="4":
        Update()
    elif ch=="5":
        Delete()
    elif ch=="6":
        while True:
            MenuTransaction()
            ch1=input("Enter choice a/b/c")
            if ch1 in ['a','A']:
                Debit()
            elif ch1 in ['b','B']:
                Credit()
            elif ch1 in ['c','C']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="7":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered")
