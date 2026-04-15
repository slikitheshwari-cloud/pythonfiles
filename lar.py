def largestofthreenumbers(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    else:
        return c

print("enter 3 three numbers: ")
n1=float(input())
n2=float(input())
n3=float(input())
print("Largest of three numbers: ",largestofthreenumbers(n1,n2,n3))
