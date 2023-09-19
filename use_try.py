"""fibo"""
a=0
b=5
n=10
while n-2:
    c=a + b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
print("\n")
"""count numbers"""
num=1234
count=0
while num>0:
    num=num//10
    count=count+1
print(count)
print(end="")
"""sum numbers"""
def get_sum(e):
    s=0
    for i in str(e):
        s += int(i)
    return(s)
print(get_sum(1234))
print(end="")
"""sum of 100"""
sun=0
for v in range(1,101):
    sun=sun+v
print(sun)





