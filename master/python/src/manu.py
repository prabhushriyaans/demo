from Matrix import M 
from DSA import Stack as S
from DSA import Queue as Q
X=[[1,2,1],[20,5,9],[50,10,2]]
Y=[[3,4,5],[11,12,15],[30,60,22]]
MO=M(x=Y,y=X)
Mp=MO.mul()
Ma=MO.addition()
Ms=MO.subtraction()
for i in range(len(X)):
    for j in range(len(X[0])):
        print(f"{X[i][j]}",end=" ")
    print()
print()
for i in range(len(Y)):
    for j in range(len(Y[0])):
        print(f"{X[i][j]}",end=" ")
    print()
print("Product:")
for i in range(len(Mp)):
    for j in range(len(Mp[0])):
        print(f"{Mp[i][j]}",end=" ")
    print()
print("addition:")
for i in range(len(Ma)):
    for j in range(len(Ma[0])):
        print(f"{Ma[i][j]}",end=" ")
    print()
print()

