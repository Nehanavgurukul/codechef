
# for prime number  right 
n=int(input("enter the number"))
if(n>1):
    i=2
    while(i<n):
        if(n%i==0):
            print("not  prime")
            break
        i=i+1
    else:
        print("yes prime")
else:
    print("not prime")
       
