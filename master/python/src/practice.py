# import mysql.connector as con
import math
name="shriyaans"
for i in name:
    print(f"{i}",end=" ")

print()
s=[1,2,3,4,5,5,5,6,7,8,8,9,9,9,10]
s=set(s)
print(s)
I=5
I **=2
print(I)
x=2>1 and 3<100 and 4>5
print(x)
if 11 not in s:
    print("True") 
l=[1,2,3,4,5,6,0,7,8,9]
for i in range(len(l)):
    if l[i]==0:
        continue
    print(f"{l[i]}",end=" ")
# while True:
#     print("hacked")
#     i=input()
#     if i=="quit":
#         break
l=[1,2,3,"Shriyaans"]
print([l[i] for i in range(len(l))])
LST=[[1,2,3,4,],[5,6],[10]]
print(LST[1][0])
matrix=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
rsum=[]
rsum_l=[]
for i in range(len(matrix)):
    rs=0
    for j in range(len(matrix[i])):
        rs+=matrix[i][j]
        if i==j:
            sum +=matrix[i][j]
        print(f"{matrix[i][j]}",end=" ")
    rsum_l.append(rs)
    print()
print(f"Sum of diagonal elements is {sum}")
print(f"Row sums are {rsum_l}")
num=int(input("Enter a number: "))
    c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c<=2:
    print(f"{num} is a prime number")
    prime=True
else:
    print(f"{num} is not a prime number")
    prime=False
m=[]
for i in range(4):
    row=[]
    for j in range(4):
        if prime==True:
            row.append(num)
    m.append(row)
print(m)

