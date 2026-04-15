def armstrong(n,len):
    n1=0
    for i in str(n):
        n1=n1+int(i)**len
    return "armstrong" if n1==n else "not a armstrong"
for i in range(10000):
    if armstrong(i,len):
        print(i)
n=int(input("enter a number: "))
len=len(str(n))
armstrong(n,len)
