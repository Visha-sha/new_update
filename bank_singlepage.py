import xlwt
import xlrd
import mysql.connector
db=mysql.connector.connect(host="localhost",
                           user="root",
                           password="mysql1234",
                           database="BANKATM_PROJECT")
cur=db.cursor();

class DB():
    def account_summary(self):
        num=int(input("enter the account:"))
        try:
            query="select name,account,balance from mogappair_bank where account={0}".format(num)
            cur.execute(query)
            data=cur.fetchall()
            #print(data)
            if len(data)>0:
                print("name:",data[0][0])
                print("account:",data[0][1])
                print("balance:",data[0][2])
        except Exception as e:
            print(e)
    def withdraw_amount(self):
        num=int(input("enter the account:"))
        amt=int(input("enter the amount to withdraw:"))
        try:
            query="select  name,account,balance from mogappair_bank where account={0}".format(num)
            cur.execute(query)
            data=cur.fetchall()
            if len(data)>0:
                query="update mogappair_bank set balance=balance-{0} where account={1}".format(amt,num)
                cur.execute(query)
                db.commit()
                print("withdraw amount successfully")
            else:
                print("details not match")
        except Exception as e:
            print(e)
    def deposit_amount(self):
        num = int(input("enter the account:"))
        amt = int(input("enter the amount to deposit:"))
        try:
            query = "select name,account,balance from mogappair_bank where account={0}".format(num)
            cur.execute(query)
            data = cur.fetchall()
            if len(data) > 0:
                query = "update mogappair_bank set balance=balance+{0} where account={1}".format(amt,num)
                cur.execute(query)
                db.commit()
                print("withdraw amount successfully")
            else:
                print("details not match")
        except Exception as e:
            print(e)
    def add_account(self):
        name=input("enter the name:")
        num=int(input("enter the account:"))
        balance=int(input("enter the balance:"))
        try:
            query="insert into mogappair_bank (name,account,balance) values('{0}',{1},{2})".format(name,num,balance)
            cur.execute(query)
            db.commit()
            print("add account successfully")
        except Exception as e:
            print(e)
    def transfer_account(self):
        num1=int(input("enter the from account:"))
        num2=int(input("enter the to account:"))
        amt=int(input("enter the amount:"))
        try:
            query1="update mogappair_bank set balance=balance-{0} where account={1}".format(amt,num1)
            query2="update mogappair_bank set balance=balance+{0} where account={1}".format(amt,num2)
            cur.execute(query1)
            cur.execute(query2)
            db.commit()
            print("amount transfered successfully")
        except Exception as e:
            print(e)

    def delete_account(self):
        num=int(input("enter the account:"))
        try:
            query="delete from mogappair_bank where account={0}".format(num)
            cur.execute(query)
            db.commit()
            print("deleted successfully")
        except Exception as h:
            print(h)
    def write_excel(self):
        try:
            query="select name,account,balance from mogappair_bank"
            cur.execute(query)
            data=cur.fetchall()
            book = xlwt.Workbook(encoding="utf-8")
            sheet=book.add_sheet("sheet")

            sheet.write(0,0,"name")
            sheet.write(0,1,"account")
            sheet.write(0,2,"balance")

            for i in range(len(data)):
                sheet.write(i+1,0,data[i][0])
                sheet.write(i+1,1, data[i][1])
                sheet.write(i+1,2, data[i][2])
            book.save("bank_bank.xls")
            print("account created successfully")
        except Exception as e:
            print(e)
    def read_excel(self):
        try:
            workbook=xlrd.open_workbook("bank_bank.xls")
            sheet=workbook.sheet_by_name("sheet")
            for i in range(1,sheet.nrows):
                name=sheet.cell(i,0).value
                num = sheet.cell(i,1).value
                balance= sheet.cell(i,2).value
                query="insert into mogappair_bank(name,account,balance) values('{0}',{1},{2})".format(name,num,balance)
                cur.execute(query)
            db.commit()
            print("read succesfully")
        except Exception as e:
            print(e)

while True:
    print(''' welcome to atm project
        1. Account Summary
        2. Withdraw Amount
        3. Deposit Amount
        4. Add account
        5. Transfer account
        6. Delete account
        7. Write excel
        8. Read excel
        9. Exit''')
    option= int(input("choose option:"))
    obj= DB()

    if option==1:
        obj.account_summary()
    elif option==2:
        obj.withdraw_amount()
    elif option==3:
        obj.deposit_amount()
    elif option==4:
        obj.add_account()
    elif option==5:
        obj.transfer_account()
    elif option==6:
        obj.delete_account()
    elif option==7:
        obj.write_excel()
    elif option==8:
        obj.read_excel()
    else:
        print("existing program")
        break;

