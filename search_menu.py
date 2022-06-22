def DispSearchAcc(): #Function to Search for the Record from the File with respect to the account number
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the accountno to be searched")
        for i in S:
            if i[0]==ch:
                print("="*125)
                F="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*125)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
        else:
            print("Record Not found")
    except:
        print("Table doesn't exist")
