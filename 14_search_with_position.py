num=int(input("Enter a number: "))
key=int(input("Enter a digit to search: "))

flag=0
v=1
pos=0

while num!=0:
    d=int(num%10)
    num=num//10
    if key==d:
        flag=1
        pos=v*d
        pos=pos//d
    v=v*10
    

if flag==1:
    print("Found and position is: ", pos,"th")
else:
    print("Not Found!!!")