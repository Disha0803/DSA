n=int(input("Enter the number of elements you want to enter: "))
print("Enter",n,"numbers")
list=[]

max=0
for i in range(n):
    list.append(int(input()))
min=list[0]

# for i in range(n):
#     if list[i]<min:
#         min=list[i]
#     if list[i]>max:
#         max=list[i]

for i in list:
    if i<min:
        min=i
    if i>max:
        max=i

print("Maximum Number= ",max, "Minimum Number= ",min)