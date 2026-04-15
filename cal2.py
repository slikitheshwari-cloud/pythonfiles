def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "error division by zero"
    else:
        return a//b
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print("calulator")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("enter your choice: ")
choice=int(input("Enter your choice: "))
if choice==1:
    print("result:",add(num1,num2))
elif choice==2:
    print("result:",sub(num1,num2))
elif choice==3:
    print("result:",mul(num1,num2))
elif choice==4:
    print("result:",div(num1,num2))
else:
    print("Invalid choice")


