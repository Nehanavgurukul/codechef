num=int(input("inter the number "))
i=1
j=1
while(0<num):
    if(i%2==0):
        print(i,end=" ")
    else:
        print(j*10,end=" ")
        j=j+1
    i=i+1
    num=num-1