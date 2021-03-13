list=["a",1,"2",5,"b","q"]
N=int(input("enter the num"))
i=0
leng=len(list)-N
while(i<N):
    print(list[leng])
    N=N-1
    leng=leng+1
    