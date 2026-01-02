from itertools import groupby
import random

s = input()


def ans_1():
    temp, ans = 0, 0
    acgt = {"A", "C", "G", "T"}
    for i in range(len(s)):
        if s[i] in acgt:
            temp += 1
            ans = max(ans, temp)
        else:
            temp = 0
    print(ans)


def ans_2():
    def check(c):
        return c in "AGCT"

    ans = 0
    for k, grp in groupby(s, check):
        temp = len(list(grp))
        if k:
            ans = max(ans, temp)

    print(ans)


def ans_3():
    temp, ans = 0, 0
    for c in s:
        if c in "AGCT":
            temp += 1
            ans = max(ans, temp)
        else:
            temp = 0
    print(ans)


method = random.randrange(3)
if method == 0:
    ans_1()
elif method == 1:
    ans_2()
else:
    ans_3()
