d={}
n=int(input("Enter number of key_value pairs:"))
for i in range(n):
    key=input("Enter key to append:")
    value=input("Enter value to append:")
    d[key]=value
print("Dictionary after creation:",d)
update_key=input("Enter key to update:")
update_value=input("Enter updated value:")
print("Dictionary  after updation:",d)
del_ele=input("Enter key to delete:")
print("Dictionary after deletion:",d)


