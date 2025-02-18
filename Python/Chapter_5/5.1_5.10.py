
print("\n" , '-' * 30, "Chapter 5", '-' * 30, "\n")

class Chapter_5_10():

    def ex_5_10(self):
        print("\n" , '-' * 30, "Exercize №10", '-' * 30, "\n")
        for a in range(1,21):  
            print(f'{a} usd  -  {a * 100} rub')

    def ex_5_9(self):
        print("\n" , '-' * 30, "Exercize №9", '-' * 30, "\n")
        print("Inch     Cm")
        for i in range(1,10):
            print(f"{i}        {round(i*2.54, 2)}")

    def ex_5_8(self):
        print("\n" , '-' * 30, "Exercize №8", '-' * 30, "\n")
        print("Pound     Kg")
        for i in range(1,10):
            print(f"{i}         {round(i*0.453, 2)}")

    def ex_5_7(self, x):
        print("\n" , '-' * 30, "Exercize №7", '-' * 30, "\n")
        for i in range (2,20):
            print(f"{i} - {round(x*i, 2)}")

    def ex_5_6(self):
        print("\n" , '-' * 30, "Exercize №6", '-' * 30, "\n")

    def ex_5_5(self):
        print("\n" , '-' * 30, "Exercize №5", '-' * 30, "\n")

    def ex_5_4(self):
        print("\n" , '-' * 30, "Exercize №4", '-' * 30, "\n")
        print(f'a           b')  
        for a in range(10,26):  
                for b in range(25,36):  
                    print(f'{a}  {a}.4', "  ", f'{b}  {b}.5  {b}.8')

    def ex_5_3(self, x, y):
        print("\n" , '-' * 30, "Exercize №3", '-' * 30, "\n")
        print("\nType 1")
        for i in range(x,y):  
            print(i)

        print("\nType 2")
        a = int(input("Set a "))  
        for i in range(a,51):  
            print(i**2)

        print("\nType 3")
        b = int(input("set b "))
        for i in range(10, b):
            print(a**3)

        print("\nType 4")
        a1 = int(input("set a "))
        b1 = int(input("set b "))
        for i in range(a1, b1):  
            print(i)

    def ex_5_2(self):
        print("\n" , '-' * 30, "Exercize №2", '-' * 30, "\n")
        a = str(input("Set a "))
        b = int(input("Set b "))
        res = (a + " ") * b
        print(res)

    def ex_5_1(self, x, y):
        x = str(x) 
        b = (x + " ") * y
        print("\n" , '-' * 30, "Exercize №1", '-' * 30, "\n")
        print(b)


chapter_5 = Chapter_5_10()
#chapter_5.ex_5_10()
chapter_5.ex_5_9()
chapter_5.ex_5_8()
#chapter_5.ex_5_7(20.4)
#chapter_5.ex_5_6()
#chapter_5.ex_5_5()
#chapter_5.ex_5_4()
#chapter_5.ex_5_3(20, 35)
#chapter_5.ex_5_2()
#chapter_5.ex_5_1(20, 10)