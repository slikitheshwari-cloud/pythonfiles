def divisors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return "prime" if len(res)==2 else "not a prime"
    

n=int(input("enter a number: "))
print(divisors(n))

    
