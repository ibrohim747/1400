class Chapter_5_50():
    def ex_5_47(self, n):
        if n == 1 or n == 2:
            return 0
        elif n == 3:
            return 1.5

        v = [0, 0, 1.5]

        for i in range(4, n + 1):
            vi = ((i - 1) / (i**2 + 1)) * v[-1] - v[-2] + v[-3]
            v.append(vi)
        
        return v[-1]


chapter_5 = Chapter_5_50()
print("Chapter 5, Ex-5.47")
print(chapter_5.ex_5_47(5))