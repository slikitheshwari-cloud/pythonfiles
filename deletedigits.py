def deletedigits(s):
    v="123456789"
    cv=0
    a=[]
    for i in s:
        if i not in v:
            cv+=1
            a.append(i)
    return a,cv

s=input("enter a string: ")
print(deletedigits(s))


