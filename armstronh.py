n=int(input("enter a number: "))
len=len(str(n))
n1=0
for i in str(n):
    n1=n1+int(i)**len
print("armstrong" if n1==n else "not a armstrong")
