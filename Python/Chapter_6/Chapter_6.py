class Chapter_6():
    print("\n",'-' * 20, "Chapter №6", '-' * 20)

    def ex_6_2(self, n):
        print("\nExercise N2")
        res = 0
        if isinstance(n, float):
            print("Somesing gona wrong")
        else:
            while(n != 0):
                res = res + 1
                n = n - 1
                print(res)
    
    def ex_6_1(self, a, b):
        print("\nExercise N1")
        division = 0
        for i in range(0,a):
            if a >= b:
                division = division + 1 if isinstance(a - b, int) else division * 1
                res_n = a - b
                a = a - b
        print(division, res_n)
    


res = Chapter_6()


res.ex_6_2(45)

res.ex_6_1(7,2)


#Easy