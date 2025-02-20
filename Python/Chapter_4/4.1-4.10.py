import math  

class Chapter_4():
    print("\nChapter №4")

    def ex_10(self, x, y):
        x = x * 1000
        y = y * 0.3048
        if x > y:
            print("X > Y")
        elif x == y:
            print("X = Y")
        else:
            print("X < Y")

    def ex_09(self):
        pass

    def ex_08(self):
        pass

    def ex_07(self, x):
        print("\n",'-' * 20, 4.7, '-' * 20)
        if math.sin(x) < 0:
            k = x**2
        else:
            if x < 0:
                k = -x
            else:
                k = x
        if k < x:
            f = k * x
        else:
            f = k + x
        print("\nF = ", f)

    def ex_06(self, x):
        print("\n",'-' * 20, 4.6, '-' * 20)
        print("A")
        if x > 2:
            print("Y = ", 2)
        else:
            print("Y = ", x)
        print("B")
        if x > 3:
            print("Y = ", -3)
        else:
            print("Y = ", -x)

    def ex_05(self, x, y):
        print("\n",'-' * 20, 4.5, '-' * 20)
        if y > 0:
            if x > 0:
                print("I\n")
            else:
                print("II\n")
        elif y < 0:
            if x > 0:
                print("IV\n")
            else:
                print("III\n")
        else:
            print("Zero\n")

    def ex_04(self, x, y):
        print("\n",'-' * 20, 4.4, '-' * 20)
        if x > 4:
            if y > 0:
                print("II\n")
            else:
                print("IV\n")
        elif x < 4:
            if y > 0:
                print("I\n")
            else:
                print("III\n")
        else:
            print("Zero\n")

    def ex_03(self, x):
        print("\n",'-' * 20, 4.3, '-' * 20)
        if x > 0:
            y = round(math.sin(x**2), 2)
        else:
            y = round(1 + 2 * math.sin(x**2), 2)
        print("Y = ", y,"\n")

    def ex_02(self, x):
        print("\n",'-' * 20, 4.2, '-' * 20)  
        if x > 0:  
            y = round(math.sin(x)**2, 2)
        else:  
            y = round(1 - 2*math.sin(x)**2, 2)  
        print(y, "\n")

    def ex_01(self, x, y):
        print("\n",'-' * 20, 4.1, '-' * 20)
        if x > y:  
            print(f"Число {x} больще числа {y}\n")
        else:
            print(f"Число {y} больще числа {x}\n")



example = Chapter_4()
example.ex_10(5, 5425)
example.ex_09()
example.ex_08()
example.ex_07(4)
example.ex_06(2)
example.ex_05(4,6)
example.ex_04(5,7)
example.ex_03(4)
example.ex_02(3)
example.ex_01(4,5)