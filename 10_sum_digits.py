num=int(input("Enter a number: "))
sum=0
while num!=0:
    d=int(num%10)
    sum+=d
    num=num//10
    print(d,"+", end=' ')

print("=",sum)



