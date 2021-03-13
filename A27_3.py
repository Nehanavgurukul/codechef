list=[]
n=int(input("enter the number"))
l=n
while(0<n):
    num=int(input("enter the number"))
    list.append(num)
    n=n-1
i=0
j=1
while(l>1):
    if(list[j]-list[i]==1):
        l-=1
        j+=1
        i+=1
    else:
        print("false")
        break
else:
    print("true")