n=int(input("enter a number: "))
fact=1
if n==0:
    fact=1
else:
    for i in range(2,n+1):
        fact=fact*i

    print(fact)



