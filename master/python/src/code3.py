Ls=[12,34,10,4,5,100,9000,2,1]
Ls2=[12,34,10,4,5,100,9001,2,1,103,17,11,0,51,30,20,41]
s_Ls=sorted(Ls)
print(s_Ls[len(s_Ls)-2])
for i in range(len(s_Ls)-1,-1,-1):
    # if i==len(s_Ls)-2:
        print(f"{i}:",end="")
        print(f" {s_Ls[i]}",end=" ")
string=input("Enter a string: ")
count=0
for i in string:
    if i in "AEIOUaeiou":
        count+=1
print(f"Number of vowels in the string is: {count}")
for i in Ls2:
    if i%2!=0:
        print(f"{i}",end=" ")
    elif i==0:
        break