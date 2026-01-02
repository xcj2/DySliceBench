import sys
sys.setrecursionlimit(2000)

def check_2(num):
    if num % 2 != 0:
        return 0
    return check_2(num // 2) + 1


def check_5(num):
    if num % 5 != 0:
        return 0
    return check_5(num // 5) + 1


def f_2(num):
    if num < 2:
        return 0
    return f_2(num - 2) + check_2(num)


def f_5(num):
    if num < 5:
        return 0
    return f_5(num - 2) + check_5(num)


N = int(input())
if N < 10:
    print(0)
    exit()
if N % 2 != 0:
    print(0)
    exit()
i = 1
ans = 0
while N // ((5 ** i) * 2) > 0:
    ans += N // ((5 ** i) * 2)
    i += 1
print(ans)
