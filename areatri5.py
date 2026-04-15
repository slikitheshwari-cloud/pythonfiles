import math
def areatri(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

print("enter values of 3 sides: ")
a=int(input())
b=int(input())
c=int(input())
print(areatri(a,b,c))
    
