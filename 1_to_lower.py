str=input("Enter a string: ")
l=len(str)
newstr=''

for i in range(l):
    newstr+=str[i].lower()

# for i in str:
#     newstr+=i.lower()

print(newstr)

# print(str.lower())
