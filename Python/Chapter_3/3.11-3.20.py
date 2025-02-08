import math


print("\n" , '-' * 30, "3.11 - 3.20", '-' * 30, "\n")

def task_3_20(x1):
    pass

def task_3_19(x1):
    pass

def task_3_18(x1):
    pass

def task_3_17(x1):
    pass

def task_3_16(x1):
    pass

def task_3_15(number):
    t1_yarus = math.ceil(number / 120)  
    t1_sectsia = math.ceil((number - 120 * (yarus - 1)) / 15)

    t2_yarus = number - 10 * (math.ceil(number / 10) -1)  
    t2_sectsia = math.ceil(number / 150)  

    return t1_yarus, t1_sectsia, t2_yarus, t2_sectsia

def task_3_14(x1):
    pass

def task_3_13(number):
    pass

def task_3_12(apartment_number):
    return (apartment_number - 1) // 4 + 1

def task_3_11(x_month, x_days):
    base_year = 1990
    past_year = math.floor(x_month / 12)
    year = base_year + past_year
    month = x_month % 12
    return year, month, x_days


place_1, place_2, place_3, place_4 = task_3_15(42)
print(f"\nResults for 3.15: Place = {place_1}, {place_2}, {place_3}, {place_4}")

h_weight = task_3_14(516)
print(f"\nResults for 3.14: ??? = {h_weight}")

h_weight = task_3_13(516)
print(f"\nResults for 3.13: ??? = {h_weight}")

floor = task_3_12(13)
print(f"\nResults for 3.12: Floor = {floor}")

year, month, days = task_3_11(42, 2)
print(f"\nResults for 3.11: Year = {year}, month = {month}, days = {days}\n")