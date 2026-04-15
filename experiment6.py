import numpy as np
import statistics
data=[]
n=int(input("Enter no of values:"))
for i in range(n):
    value=float(input("Enter value to appended:"))
    data.append(value)
arr=np.array(data)
print("\n Data:",arr)
mean=np.mean(arr)
median=np.median(arr)
mode=statistics.mode(arr)
var=np.var(arr)
std_dev=np.std(arr)
print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)
print("Variance:",var)
print("standard deviation:",std_dev)
