SP = int(input("enter the selling price"))
CP = int(input("enter the cost price"))

if(SP > CP ):
    print("Profit")
elif(CP > SP):
    print("Loss")
else:
    print("no profit, no loss")