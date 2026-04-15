def countvowels(s):
    v="aeiouAEIOU"
    cv=0
    for i in s:
        for i in v:
            cv+=1
    return cv

s=input("enter a string: ")
print("Total no of vowels in ",s,"is:\n",countvowels(s))
