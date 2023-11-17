num=int(input("Enter a number: "))
n=num
rev=0
while num!=0:
    d=int(num%10)
    rev=rev*10+d
    num=int(num/10)

if rev==n:
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")

