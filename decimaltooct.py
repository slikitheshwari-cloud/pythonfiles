def decimalTooct(d):
    d=int(d,10)
    return oct(d)
n=input("enter decimal number: ")
print("equilvalent octal number: ",decimalTooct(n))
