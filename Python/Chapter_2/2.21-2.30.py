from math import sqrt, sin, degrees, atan

print('-' * 30, "2.21 - 2.30", '-' * 30)

def caluclate_2_30(x1, y1, x2, y2, x3, y3, x4, y4):
    area1 = caluclate_2_29(x1, y1, x2, y2, x3, y3)
    area2 = caluclate_2_29(x1, y1, x3, y3, x4, y4)
    return area1 + area2

def caluclate_2_29(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def caluclate_2_28(a, b):
    return degrees(atan((a - b) / 2))

def caluclate_2_27(top_side, down_side, hight):
    return (top_side + down_side) / 2 * hight

def caluclate_2_26(x1, x2, y1, y2):
    x_side = y1 - x1
    y_side = y2 - x2
    distance = sqrt((x_side ** 2) + (y_side ** 2))
    return distance

def caluclate_2_25(width, hight, length):
    volume = width * hight * length
    side_surface_area = 2 * (width * hight + hight * length + width * length)
    return volume, side_surface_area

def caluclate_2_24(a, b):
    sum = a + b
    difference = a - b
    division = a * b
    remains = a / b if b!= 0 else 'Error: Division by zero'
    return sum, difference, division, remains

def caluclate_2_23(a, b):
    diogonal = sqrt(a ** 2 + b ** 2)
    P = a * 2 + b + 2
    return diogonal, P

def caluclate_2_22(num_1, num_2):
    geometric_mean = sqrt(num_1 + num_2)
    arithmetic_mean = (num_1 + num_2)
    return geometric_mean, arithmetic_mean

def caluclate_2_21(e,f,g,h):
    a = ( e + (f/2) ) / 3
    b = (h ** 2) - g
    c_1 = abs((g - h)**2 - (3 * sin(e)))
    c = sqrt(c_1)
    return a, b, c

area = caluclate_2_28(12, 3)
print(f"\nResults for 2.28: Area = {area}")

perimeter = caluclate_2_27(4, 9, 7)
print(f"\nResults for 2.27: Perimeter of the tropezia = {perimeter}")

distance = caluclate_2_26(3,6,7,2)
print(f"\nResults for 2.26: Distance between 2 points in 2d space = {distance}")

volume, perimeter = caluclate_2_25(3,5, 7)
print(f"\nResults for 2.25: Volume = {volume}, Perimeter all sides = {perimeter}")

sum, difference, division, remains = caluclate_2_24(3,4)
print(f"\nResults for 2.24: Summ = {sum}, Difference = {difference}, Division = {division}, Remains = {remains}")

diogonal, perimeter = caluclate_2_23(3,6)
print(f"\nResults for 2.23: Rectangle diagonal = {diogonal} and perimeter = {perimeter}")

math_mean, geom_mean = caluclate_2_22(3,4)
print(f"\nResults for 2.21: Arithmetic mean = {math_mean}, Geometric mean = {geom_mean}")

a, b, c = caluclate_2_21(2,3,4,5)
print(f"\nResults for 2.20: a = {a}, b = {b}, c = {c}\n")