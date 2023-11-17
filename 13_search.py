num=int(input("Enter a number: "))
key=int(input("Enter a digit to search: "))

flag=0

while num!=0:
    d=int(num%10)
    if key==d:
        flag=1
        break
    num=int(num/10)

if flag==1:
    print("Found :)")
else:
    print("Not Found!!!")