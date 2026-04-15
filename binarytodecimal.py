def binaryToBinary(d):
    d=int(d,10)
    return bin(d)[2:]
n=input("enter decimal number: ")
print("equilvalent binary number: ",decimalToBinary(n))
