n=int(input("Enter the number of elements you want to enter: "))
print("Enter",n,"numbers")
list=[]
sum=0
for i in range(n):
    list.append(int(input()))

# for i in range(n):
#     sum+=list[i]

for i in list:
    sum+=i

print("Sum of the numbers= ",sum)