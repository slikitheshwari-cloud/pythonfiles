string = input("Enter a string: ")
char = input("Enter a character: ")

count = 0
for c in string:
    if c == char:
        count+=1
print(f"frequencys of '{char}' is:",count)

a=input("Enter a string: ")
char=input("Enter a character: ")
print("Frequency:",a.count(char))
