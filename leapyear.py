def leapyear(year):
     if year%4==0 or year%100!=0 or year%400==0:
         return "leapyear"
     else:
         "not a leap year"

year=int(input("enter a year: "))
print(leapyear(year))
 
