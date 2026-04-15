with open(r"M:\1st semester\notes.txt","r") as file:
    v="aeiou"
    f=file.read()
    if i in v:
        f=f.replace('v','')
print(f)
