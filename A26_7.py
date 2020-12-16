
i=1
k=1
while(i<=5):
    j=1
    p=k
    while(j<=i):
        print(p,end=" ")
        j=j+1
        p=p+1
    l=i-1
    while(l>0):
        print(p-2,end=" ")
        p=p-1
        l=l-1
    print()
    i=i+1
    k=k+1