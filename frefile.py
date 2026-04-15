from collections import Counter
with open(r"M:\1st semester\notes.txt","r") as file:
    words=file.read().split()

frequency=Counter(words)
print(frequency)
