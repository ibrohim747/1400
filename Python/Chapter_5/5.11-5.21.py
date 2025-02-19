import math
import numpy as np

print("\n" , '-' * 30, "Chapter 5", '-' * 30, "\n")

class Chapter_5_20():
    def ex_5_20(self):
        print("\n" , '-' * 30, "Exercize N20", '-' * 30, "\n")
        for i in range(1,9):
            i = round(i * 0.1, 1)
            print(round(math.sqrt(i), 2))

    def ex_5_19(self):
        print("\n" , '-' * 30, "Exercize N19", '-' * 30, "\n")
        for i in np.arange(0.1, 1.6, 0.1):
            print(f"sin {i:.2f} = {math.sin(i):.2f}\n")

    def ex_5_18(self):
        print("\n" , '-' * 30, "Exercize N18", '-' * 30, "\n")
        for a in range(2,18):  
            t = 3 * a  
            z = 3*t**2 + 4.87*t - 3  
            print(f't = {t}, z = {z}')

    def ex_5_17(self):
        print("\n" , '-' * 30, "Exercize N17", '-' * 30, "\n")
        for x in range(4,29):
            t = x + 3
            y = (3 * t)**2 + 4.87*t - 3
            print(f"x = {x}: t = {t}, y = {y:.2f}")
    
    def ex_5_16(self):
        print("\n" , '-' * 30, "Exercize N16", '-' * 30, "\n")
        for a in range(12,16):  
            b = round(math.sin(a),2)  
            print(f' sin {a} = {b}')

    def ex_5_15(self):
        print("\n" , '-' * 30, "Exercize N15", '-' * 30, "\n")
        b = int(input("Set a number "))
        for a in range(1,10):  
            print(f' {b} * {a} = {a*b}')
    
    def ex_5_14(self):
        print("\n" , '-' * 30, "Exercize N14", '-' * 30, "\n")
        for a in range(1,10):  
            print(f' 9 * {a} = {a*9}')

    def ex_5_13(self):
        print("\n" , '-' * 30, "Exercize N13", '-' * 30, "\n")
        for a in range(1,10):  
            print(f' {a} x 7 = {a*7}')

    def ex_5_12(self):
        print("\n" , '-' * 30, "Exercize N12", '-' * 30, "\n")
        AIR_DENSITY = 1.29 #kg/m3
        k = 1.25e-4  # 1/m
        #The dependence of air density on altitude = P = p0 * e**(-h*z)
        print("Height (m)\tDensity (kg/m3)")
        for d in range(0, 1100, 100):
            density_by_height = AIR_DENSITY * math.exp(-k * d)
            print(f"{d}\t\t{density_by_height:.5f}")
        
    def ex_5_11(self):
        print("\n" , '-' * 30, "Exercize N11", '-' * 30, "\n")
        R = 6350 #km
        print("Height (km)\tDistance to the horizon")
        for h in range(1,11):
            d = math.sqrt((R + h) ** 2 - R ** 2)
            print(f"{h}\t\t{d:.2f}")



chapter_5 = Chapter_5_20()
chapter_5.ex_5_20()
chapter_5.ex_5_19()
chapter_5.ex_5_18()
chapter_5.ex_5_17()
chapter_5.ex_5_16()
chapter_5.ex_5_15()
chapter_5.ex_5_14()
chapter_5.ex_5_13()
chapter_5.ex_5_12()
chapter_5.ex_5_11()

#5.11-5.21.py