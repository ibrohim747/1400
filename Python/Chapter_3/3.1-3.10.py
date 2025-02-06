import math
print("\n" , '-' * 30, "3.1 - 3.10", '-' * 30, "\n")

def task_3_10(x1):
    pass

def task_3_9(n):
    hours = n // 3600
    minutes = (n % 3600) // 60
    seconds = n % 60
    return hours, minutes, seconds

def task_3_8(x1):
    ticket_number = int(x1)
    place_in_one_row = 15
    rows = 20
    num_first_place = int("01643")
    priority = ticket_number - num_first_place
    row_num = math.ceil(priority / place_in_one_row)
    if row_num > rows:
        return "Error. Something gonna wrong"
    else:
        return row_num

def task_3_7(apartment_num):
    levels = 5
    per_level = 15
    total_apartments = levels * per_level
    apartment_level = math.ceil(apartment_num / per_level)
    if apartment_num > total_apartments:
        return "Error. Something gonna wrong"
    else:
        return apartment_level

def task_3_6(seat_num):
    compartment = 9
    set_number_per_compartment = 4
    total_sets = compartment * set_number_per_compartment
    set_compartment = math.ceil(seat_num / set_number_per_compartment)
    if seat_num > total_sets:
        return "Error. Something gonna wrong"
    else:
        return set_compartment

def task_3_5(x1):
    weidth = 543
    length = 130
    from_weidth = weidth // x1
    from_length = length // x1
    quantity = from_length * from_weidth
    return quantity

def task_3_4(schoolchild, apples):
    apple_per_schold = apples // schoolchild
    remain_apple = apples % schoolchild
    return apple_per_schold, remain_apple

def task_3_3(days):
    weeks = days // 7
    return weeks

def task_3_2(a):
    hundredweight = a // 100
    return hundredweight

def task_3_1(a):
    meter = a // 100
    return meter


weeks = task_3_10(234)
print(f"\nResults for 3.10: Pasted weeks = {weeks}")

h, m, s = task_3_9(25000)
print(f"\nResults for 3.9: Total hours: {h}, total minutes in the current hour: {m}, total seconds in the current minute: {s}")

row_num = task_3_8("01659")
print(f"\nResults for 3.8: Row number = {row_num}")

apt_level = task_3_7(54)
print(f"\nResults for 3.7: Apartment in level = {apt_level}")

comp_num = task_3_6(13)
print(f"\nResults for 3.6: Compartment number = {comp_num}")

quantity = task_3_5(130)
print(f"\nResults for 3.5: Total quantity = {quantity}")

per_apple, r_apple = task_3_4(7, 22)
print(f"\nResults for 3.4: Apple per school child = {per_apple}, remainding apple = {r_apple}")

weeks = task_3_3(234)
print(f"\nResults for 3.3: Pasted weeks = {weeks}")

h_weight = task_3_2(516)
print(f"\nResults for 3.2: Hundredweight = {h_weight}")

m = task_3_1(352)
print(f"\nResults for 3.1: Meter = {m}\n")