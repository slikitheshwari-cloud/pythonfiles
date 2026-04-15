friends={
    "likitha":"watching tv"
}

n=int(input("Enter no of friends: "))
for i in range(1,n+1):
    k=input("Enter key : ")
    v=input("Enter value: ")
    friends[k]=v

print(friends)
