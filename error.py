with open(r"M:\1st semester\notes.txt","r") as file:
    for line in file:
        if "error" in line.lower():
            print(line.strip())
