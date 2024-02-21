from math import sin
from math import radians
from math import cos

sides_num = float(input("Input number of sides: "))
len_  = float(input("Input the length of a side: "))
side_len = (len_/2) / cos(radians(((sides_num - 2) * 180)/(sides_num*2)))
radius = side_len * cos(radians(180 /sides_num))

area  =  round(0.5 * sides_num * len_ * radius)
print(radius)

print(f"The area of the polygon is: {area}")