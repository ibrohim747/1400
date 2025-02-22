class Chapter_5():
    print("\n",'-' * 20, "Chapter №5", '-' * 20)

    def ex_60(self, x, y):
        pass

    def ex_59(self, x, y):
        pass

    def ex_58(self, x, y):
        pass

    def ex_57(self, x, y):
        pass

    def ex_56(self, x, y):
        pass

    def ex_55(self, x, y):
        pass

    def ex_54(self, x, y):
        pass

    def ex_53(self, x, y):
        pass

    def ex_52(self, x, y):
        pass

    def ex_51(self, x, y, z, y1, y2, y3):
        self.arrea = x
        self.productivity = y
        self.find = z
        self.for_year_1 = y1
        self.for_year_2 = y2
        self.for_year_3 = y3
        self.growth_arrea = 5
        self.growth_productivity = 2

        def res_0(productivity, growth_productivity, for_year_1, for_year_2, for_year_3):
            res_year_1 = res_year_2 = res_year_3 = None  # Initialize variables
            for i in range(1, for_year_3 + 1):
                productivity *= ((growth_productivity / 100) + 1)
                if i == for_year_1:
                    res_year_1 = round(productivity, 5)
                elif i == for_year_2:
                    res_year_2 = round(productivity, 5)
                elif i == for_year_3:
                    res_year_3 = round(productivity, 5)
            return res_year_1, res_year_2, res_year_3  # Return after the loop

        def res_1(arrea, growth_arrea, for_year_1, for_year_2, for_year_3):
            res_year_1 = res_year_2 = res_year_3 = None  # Initialize variables
            for i in range(1, for_year_3 + 1):
                arrea *= ((growth_arrea / 100) + 1)
                if i == for_year_1:
                    res_year_1 = round(arrea, 2)
                elif i == for_year_2:
                    res_year_2 = round(arrea, 2)
                elif i == for_year_3:
                    res_year_3 = round(arrea, 2)
            return res_year_1, res_year_2, res_year_3  # Return after the loop

        if self.find == 0:
            year_1, year_2, year_3 = res_0(
                self.productivity, self.growth_productivity, self.for_year_1, self.for_year_2, self.for_year_3
            )
            print("\nExercise №51_A")
            print(round(year_1, 3), round(year_2, 3), round(year_3, 3))
        if self.find == 1:
            year_1, year_2, year_3 = res_1(
                self.arrea, self.growth_arrea, self.for_year_1, self.for_year_2, self.for_year_3
            )
            print("\nExercise №51_B")
            print(round(year_1, 3), round(year_2, 3), round(year_3, 3))
        if self.find == 1:
            year_1_a, year_2_a, year_3_a = res_0(
                self.arrea, self.growth_arrea, self.for_year_1, self.for_year_2, self.for_year_3
            )
            year_1_b, year_2_b, year_3_b = res_1(
                self.arrea, self.growth_arrea, self.for_year_1, self.for_year_2, self.for_year_3
            )
            print("\nExercise №51_C\n")
            print(round(year_1_a * year_1_b, 3), round(year_2_a * year_2_b, 3), round(year_3_a * year_3_b, 3))



ch_5_50 = Chapter_5()
ch_5_50.ex_51(100, 20, 0, 4, 5, 7) #A
ch_5_50.ex_51(100, 20, 1, 4, 5, 7) #B
ch_5_50.ex_51(100, 20, 2, 4, 5, 7) #C