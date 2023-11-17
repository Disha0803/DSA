start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range: "))

print("Prime numbers between ",start," & ",end)
for i in range(start,end+1):
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        print(i)