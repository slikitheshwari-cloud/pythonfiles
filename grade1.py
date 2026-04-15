
def calculategrade(marks):
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B+"
    elif marks>=60:
        return "B"
    elif marks>=50:
        return "c"
    elif marks>=40:
        return "D"
    else:
        return "F"

marks=float(input("enter marks: "))
grade=calculategrade(marks)
print("Grade=",grade)


