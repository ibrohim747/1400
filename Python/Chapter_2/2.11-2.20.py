from random import randint
import math


print('-' * 20, "2.20", '-' * 20)
e, f, g, h = 3, 2, 5, 1
a = math.sqrt(abs(e - (3 / f))**3) + g
b = math.sin(e) + math.cos(h)**2
c = (33 * g) / (e * f - 3)
print(f"a = {a}, b = {b},c = {c}")

print('-' * 20, 2.19, '-' * 20)
a, b = 2, 4
numerator_x = 2 / (a**2 + 25) + b
denominator_x = math.sqrt(b) + (a + b) / 2
x = numerator_x / denominator_x

numerator_y = abs(a) + 2 * math.sin(b)
denominator_y = 5.5 * a
y = numerator_y / denominator_y
print(x, y)

print('-' * 20, 2.18, '-' * 20)
x = randint(1,10)
y = randint(1,10)
equation_1 = round((x + (2 + y) /x ** 2) / y + (1 / math.sqrt(x ** 2 + 10)), 3)
equation_2 = round((7.25 * math.sin(x) - y),3)
#if equation_1 == True & equation_2 == True:
print(f"x = {x}, y = {y}, eq1 = {equation_1}, eq2 = {equation_2}")

print('-' * 20, 2.17, '-' * 20)
height_of_trapezoid = 4
base_of_trapezoid = 3
area = height_of_trapezoid * base_of_trapezoid
print(area)

print('-' * 20, 2.16, '-' * 20)
leg_1 = 3
leg_2 = 4
area = (leg_1 * leg_2) / 2
print(area)

print('-' * 20, 2.15, '-' * 20)
external_radius = 4
internal_radius = 3
area = round((math.pi * external_radius ** 2) - (math.pi * internal_radius ** 2),0)
print(area)

print('-' * 20, 2.14, '-' * 20)
leg_1 = 3
leg_2 = 4
hypotenuse = math.sqrt(leg_1**2 + leg_2**2)
print(hypotenuse)

print('-' * 20, 2.13, '-' * 20)
for x in range(-5,5):
    for b in range(-5,5):
        for a in range(-5,5):
            if x == 0 & b == 0 & a == 0:
                continue
            else:
                equation = a * x + b == 0
                if equation == True:
                    print(f"a = {a}, b = {b}, x = {x}")

print('-' * 20, 2.12, '-' * 20)
population = 3500000
area = 435  #km2
area_in_meter = area * 1000
density = round(population / area, 1)
print(density)

print('-' * 20, 2.11, '-' * 20)
volyune = 4 #m3
mass = 5000   #kg
density = mass / volyune
print(f"Density = {density} kg/m3")