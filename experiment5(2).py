import numpy as np
n=int(input("Enter number of elements:"))
elements=[]
for i in range(n):
    value=int(input(f"Enter element {i+1}:",))
    elements.append(value)
arr=np.array(elements)
print("\n origiinal array:",arr)
print("sliced array (index 1 to 3):",arr[1:4])
indices=[0,2]
print("Integer indexinig(0,2):",arr[indices])
print("Elemts greater than 5:",arr[arr>5])
print("Array+2:",arr+2)
print("Array*2:",arr*2)
print("Array mean:",np.mean(arr))
print("Array sum:",np.sum(arr))
