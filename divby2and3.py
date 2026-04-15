def divisibleby2and3(n):
    return "(n) divisible by 2 and 3" if n%2==0 and n%3==0 else "return not divisible by 2 and 3"
num=int(input("Enter a number; "))
print(divisibleby2and3(num))
