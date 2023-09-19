class oddeven_number:
    def __init__(self,num):
        self.num=num
    def odd_even(self):
        try:
            if self.num%2==0:
                print("the num is even")
            else:
                print("the num is odd")
        except Exception as e:
            print(e)
obj=oddeven_number(3)
obj.odd_even()
