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

operations={
    1:add,
    2:sub,
    3:mul,
    4:div
}
print("calculator")
print("1.add")
print("2.substract")
print("3.multiplication")
print("4.division")

choice=int(input("Enter your choice: "))
if choice in operations:
    x=float(input("Enter first number: "))
    y=float(input("Enter secound number: "))

    result=operations[choice](x,y)
    print("Result:",result)

else:
    print("invalid choice: ")
