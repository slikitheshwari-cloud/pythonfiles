list=[]
n=int(input("Enter no of  number to be inserted:"))
for i in range(n):
    element=int(input(f"Enter an element {i+1}:"))
    list.append(element)
print("list after creation:",list)
new_element=int(input("Enter a new element:"))
list.append(new_element)
print("list after appending:",list)
remove_element=int(input("Enter am element to remove:"))
list.remove(remove_element)
print("list after removing:",list)
