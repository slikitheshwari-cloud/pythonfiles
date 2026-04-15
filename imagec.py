import pickle

with open(r"M:\1st semester\python\a1.jpg","rb") as source:
    data=source.read()

with open(r"M:\1st semester\python\mca1.jpg","wb") as target:
    target.write(data)
print("Image copied")

