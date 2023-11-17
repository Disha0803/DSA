str=input("Enter a string: ")
l=len(str)
s=str
# rev=''

# for i in range(l-1,-1,-1):
#     rev+=str[i]

rev=str[::-1]

if rev==s:
    print(s, "is a palindrome string")
else:
    print(s, "is not a palindrome string")

