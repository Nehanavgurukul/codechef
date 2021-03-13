A = 0
B = 1
n = int(input("enter the number"))
if(n == 1):
    print(A)
else:
    if(n == 2):
        print(A,B)
    else:
        print(A,B)
        i = 0
        while(i<=n-2):
            C = A+B
            A = B
            B = C
            i = i + 1
            print(C)
            