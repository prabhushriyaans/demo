# import mysql.connector as con
name="shriyaans"
for i in name:
    print(f"{i}",end=" ")

print()
s=[1,2,3,4,5,5,5,6,7,8,8,9,9,9,10]
s=set(s)
print(s)
I=5
I**=2
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
