def fibo(n):
    a,b=0,1
    for i in range(0,n+1):
        print(f"{a}",end=" ")
        a,b=b,a+b
    print()
