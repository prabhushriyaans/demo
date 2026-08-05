m=[]
for i in range(2):
    row=[]
    for j in range(2):
        num=int(input("Enter a number: "))
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c+=1
        if c==2:
            print(f"{num} is a prime number")
            prime=True
        else:
            print(f"{num} is not a prime number")
            prime=False
        if prime==True:
            row.append(num)
    m.append(row)
print(m)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==0 and j==0 or i==len(matrix)-1 and j==len(matrix)-1:
            print(f"{matrix[i][j]}",end=" ")
        else:
            print(" ",end=" ")
    print()


