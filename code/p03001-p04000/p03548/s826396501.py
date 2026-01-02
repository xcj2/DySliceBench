import numpy as np
import math
import fractions


class KyoPro:
    AtCoder_Mod = 1000 * 1000 * 1000 + 7

    def ReadListOfNumbers():
        return list(map(int, input().split()))

    @staticmethod
    def MakeStringFromNumbers(a):
        if len(a) == 0:
            return
        s = str(a[0])

        for i in range(1, len(a)):
            s += ' ' + str(a[i])

        return s

    # 二分探索、配列、目的の値、比較の関数（必要なければNone）
    @staticmethod
    def BinarySearch(ls, target, func):
        if(func is None):
            def func(a, b): return a < b

        def eq(a, b): return (not func(a, b)) and (not func(b, a))

        left = 0
        right = len(ls) - 1

        while(True):
            if(right - left < 10):
                for i in range(left, right + 1):
                    if(eq(ls[i], target)):
                        return True
                return False

            center = (left + right) // 2
            if(eq(ls[center], target)):
                return True
            if(func(ls[center], target)):
                left = center
            if(func(target, ls[center])):
                right = center


class cin:
    InputList = []

    def __init__(self):
        pass

    def Read(self):
        cin.InputList += input().split()

    def ReadInt(self):
        if(len(cin.InputList) == 0):
            self.Read


def main():
    temp = KyoPro.ReadListOfNumbers()
    x = temp[0]
    y = temp[1]
    z = temp[2]

    y += z
    x -= z

    print(x // y)


main()
