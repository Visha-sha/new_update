class company():
    def __init__(self):
        self.companyname="IBM"
        self.companylocation="bangalore"
    def showcompany(self):
        print("company name:",self.companyname)
        print("company lovation:",self.companylocation)
c1=company()
c1.showcompany()

class employee(company):
    def __init__(self,empid,empname,dept):
        self.empid=empid
        self.empname=empname
        self.dept=dept
        company.__init__(self)
    def showemployee(self):
        print("emp_id:",self.empid)
        print("emp_name:",self.empname)
        print("department:",self.dept)
e1=employee(123,"rithu","IT")
e2=employee(456,"sha","CSE")
e1.showemployee()
e2.showemployee()
e2.showcompany()
e2.dept="CIVIL"
e2.companylocation="chennai"
e2.showemployee()
e2.showcompany()

