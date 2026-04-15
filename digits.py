def printdigits(s):
    v="123456789"
    cv=0
    a=[]
    for i in s:
        if i in v:
           a.append(i)
    return a

s=input("enter a string: ")
print(*printdigits(s))
