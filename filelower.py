a=input("Enter a string to look for: ")
with open(r"M:\1st semester\notes.txt","r") as file:
    for line in file:
        if a.upper() in line.upper():
            print(line.strip())
 
