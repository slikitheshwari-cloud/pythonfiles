fruits={
    "apple":110,
    "mango":120
}
n=int(input("Enter no of fruits you want to enter: "))
for i in range(1,n+1):
    k=input("enter a key: ")
    v=input("Enter a value: ")
    fruits[k]=v

print(fruits)
