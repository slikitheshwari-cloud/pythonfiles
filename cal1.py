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
print("+.addition")
print("-.substraction")
print("*.multiplication")
print("/.division")
print("enter your choice: ")
choice=(input("Enter your choice: "))
if choice=="+":
    print("result:",add(num1,num2))
elif choice=="-":
    print("result:",sub(num1,num2))
elif choice=="*":
    print("result:",mul(num1,num2))
elif choice=="/":
    print("result:",div(num1,num2))
else:
    print("Invalid choice")


