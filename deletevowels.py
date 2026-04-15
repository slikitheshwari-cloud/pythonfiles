def deletevowels(s):
    v="aeiouAEIOU"
    cv=0
    a=[]
    for i in s:
        if i not in v:
           a+=i
    return a

s=input("enter a string: ")
print(" deleting vowels ",s,"is:\n",deletevowels(s))
