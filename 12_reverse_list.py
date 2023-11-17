n=int(input("Enter the number of elements you want to enter: "))
print("Enter",n,"numbers")
list=[]
for i in range(n):
    list.append(int(input()))

print("Original List: ")
for i in range(n):
    print(list[i],end=' ')
print()
print("Reversed List: ")
for i in range(n-1,-1,-1):
    print(list[i], end=' ')