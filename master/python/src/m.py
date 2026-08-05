l1=[[1,2,3],[4,5,6]]
l2=[[1,2],[3,4],[5,6]]
l3=[]
for i in range(len(l1)):
    row=[]
    for j in range(len(l2[0])):
        sm=0
        for k in range(len(l2)):
            sm +=l1[i][k]*l2[k][j]
        row.append(sm)
    l3.append(row)
print(l3)
lr=[1,2,3,3,4,5,6,6,7,7,7,7,7,8,9,9,9,10,11,12,13]

for i in range(len(lr)):
    cu=0
    for j in range(len(lr)):
        if lr[i]==lr[j]:
            cu+=1
    print(f"{lr[i]} occurs {cu} times")
mx=[]
for i in range(3):
    row=[]
    for j in range(3):
        num=int(input("Enter a number: "))
        duplicate=False
        for k in range(i):
            if mx[k][j]==num:
                print(f"{num} is already present in the column {j+1}")
                duplicate=True
                break
        if not duplicate:
            row.append(num)
    mx.append(row)
for i in range(3):
    for j in range(3):
        print(f"{mx[i][j]}",end=" ")
    print()