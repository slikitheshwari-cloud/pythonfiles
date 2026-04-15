elements=[]
n=int(input("Enter no of elements:"))
for i in range(n):
    value=input(f"Enter value to be appended{i+1}:")
    elements.append(value)
t=tuple(elements)
print("\n tuple:",t)
print("\n length of tupele:",len(t))
index=int(input("Enter index to access elements:"))
print("Element at index:",index,"is",t[index])

              
      
