from bank_main import DB


class BANK():

    def accountsummary(self):
        num = int(input("enter the account number:"))
        try:
            data = DB().select(num)
            if len(data) > 0:
                print('*****account summary*****')
                print('name:', data[0][0])
                print('account:', data[0][1])
                print('balance:', data[0][2])
            else:
                print('account details not match')
        except Exception as e:
            print(e)

    def addaccount(self):
        name = input("enter the name:")
        account = int(input("enter the account no:"))
        balance = int(input("enter the balance:"))
        try:
            DB().insert(name, account, balance)
            print("account added successfully")
        except Exception as e1:
            print(e1)
            print("account details are not added")
    def deleteaccount(self):
        num = int(input("enter the account:"))
        try:
            DB().delete(num)
            print("account deleted successfully")
        except Exception as E:
            print(E)

    def withdraw_amount(self):
        num=int(input("enter the account:"))
        amt=int(input("enter the balance:"))
        try:
            DB().withdraw(num,amt)
            print("withdraw successfully")
        except Exception as ee:
            print (ee)
    def amount_transfer(self):
        num1 = int(input("enter the from account:"))
        num2 = int(input("enter the to account:"))
        amt = int(input("enter the balance:"))
        try:
            DB().transfer(num1,num2,amt)
            print("transfered successfulluy")
        except Exception as E:
            print(E)



while True:
    print('''welcome to atm project
            1. Account Summary
            2. Add account
            3. Delete account
            4. Withdraw
            5. Transfer
            6. Exit''')

    option = int(input("choose option:"))
    obj = BANK()
    if option == 1:
        obj.accountsummary()
    elif option == 2:
        obj.addaccount()
    elif option == 3:
        obj.deleteaccount()
    elif option==4:
        obj.withdraw_amount()
    elif option==5:
        obj.amount_transfer()
    else:
        print('exiting program')
        break

