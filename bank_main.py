import mysql.connector
db = mysql.connector.connect(host='localhost',
                        database='BANKATM_PROJECT',
                        user='root',
                        password='mysql1234',
                         auth_plugin='mysql_native_password')
cur = db.cursor()


class DB():

    def select(self, num):
        try:
            query = 'select name,account,balance from mogappair_bank where account={0}'.format(num)
            cur.execute(query)
            data = cur.fetchall()
            return data

        except Exception as e:
            print(e)

    def insert(self, name, num, balance):
        try:
            query = "insert into mogappair_bank(name,account,balance) values('{0}',{1},{2})".format(name, num, balance)
            cur.execute(query)
            db.commit()
            print('account added successfully')

        except Exception as e1:
            print(e1)


    def delete(self, num):
        try:
            query = "delete from mogappair_bank where account={0}".format(num)
            cur.execute(query)
            db.commit()
            print('account deleted successfully')
        except Exception as E:
            print(E)


    def withdraw(self,num,amt):
        try:
            query="select from mogappair_bank (name,account,balance) where account={0}".fromat(num)
            cur.execute(query)
            data=cur.fetchall()
            if len(data)>0:
                query = "update mogappair_bank set balance=balance-{0} where account={1}".format(num,amt)
                cur.execute(query)
                db.commit()
                print('account withdraw successfully')
            else:
                print("details not match")
        except  Exception as e2:
            print(e2)

    def transfer(self,num1,num2,amt):
        try:
            query1="update mogappair_bank set balance=balance-{0} where account={1}".format(num1,amt)
            query2 ="update mogappair_bank set balance=balance+{0} where account={1}".format(num2, amt)
            cur.execute(query1)
            cur.execute(query2)
            db.commit()
            print("tranfered successfully")
        except Exception as e3:
            print(e3)
