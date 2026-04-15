string=input("Enter a string: ")
frequency={}

for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

print("character frequency: ")
print(frequency)
