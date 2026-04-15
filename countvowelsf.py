with open(r"M:\1st semester\demo1.txt","r") as ob:
    nv=0
    data=ob.read()
    for i in data:
        if i not in "AEIOUaeiou":
            nv+=1
    print("total no of consonants: ",nv)
