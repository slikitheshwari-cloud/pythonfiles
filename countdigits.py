def countdigits(s):
    v="123456789"
    cv=0
    a=[]
    for i in s:
        if i in v:
           cv+=1
    return cv

s=input("enter a string: ")
print(countdigits(s))
