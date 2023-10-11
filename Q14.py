import math

X=complex(input("Enter first complex number: "))
Y=complex(input("Enter second complex number: "))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
ch=int(input("Enter your choice:"))
if(ch==1):
    Z=X+Y
elif(ch==2):
    Z=X-Y
elif(ch==3):
    Z=X*Y
else:
    print("Invaild choice")
print("Result = ",Z)
    
