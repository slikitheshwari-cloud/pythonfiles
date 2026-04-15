import math
def area_circle(d):
    r=d/2
    area=math.pi*pow(r,2)
    return area
d=int(input("enter diameter: "))
print(area_circle(d))

    
