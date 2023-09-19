for num in range(1,50):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")
print("\n")
for j in range(1,50):
    mon=0
    for k in range(1,j):
        if j%k==0:
            mon=mon+k
            if mon==j:
                print(j,end=" ")
print("\n")
mystr="MADAM"
if mystr==mystr[::-1]:
   print("is palindrome")
else:
   print("is not palindrome")


vowel_str="Rithvin love you"
vowels =0
for r in vowel_str:
    if (r=="a" or r=="e" or r=="i" or r=="o" or r=="u"):
        vowels=vowels+1
print(vowels)

tu=1213
temp=tu
wed=0
while (temp>0):
    digit=temp%10
    wed=wed*10+digit
    temp=temp//10
if (tu==wed):
    print("is pali")
else:
    print("is not pali")

def reverse(st):
    tr=""
    for i in st:
        tr=i+tr
    return (tr)
print(reverse("rithvin"))

x="awesome"
def myfunc():
    x="fabulous"
    print("python is" +x)
myfunc()
print("python is" +x)



def cal_avg(no):
    sum_num=0
    for i in no:
        sum_num=sum_num+i
    avg=sum_num/len(no)
    return avg
print(cal_avg([1,2,3,4]))

li=[]
n=int(input("Enter size of list:"))
for i in range(0,n):
    e=int(input("Enter element of list {0}:".format(i)))
    li.append(e)
print("second largest in ",li,"is",sum(li))


