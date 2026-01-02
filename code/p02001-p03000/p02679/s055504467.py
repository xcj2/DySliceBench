import sys
import math


stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()

AB_array = [na() for _ in range(N)]

# print(AB_array)

plus_dic = {}
minus_dic = {}
ans = 1
fish_count = 0
mod = 10 ** 9 + 7
zero_count = 0
for ab in AB_array:
    a, b = ab
    if a == 0 and b == 0:
        zero_count += 1
        continue
    fish_count += 1
    if a == 0:
        vec = (0, 1)
        if vec in plus_dic:
            plus_dic[vec] += 1
        else:
            plus_dic[vec] = 1
        continue
    elif b == 0:
        vec = (1, 0)
        if vec in minus_dic:
            minus_dic[vec] += 1
        else:
            minus_dic[vec] = 1
        continue
    c = math.gcd(a, b)
    a = a // c
    b = b // c
    if a < 0:
        a *= -1
        b *= -1
    if b > 0:
        vec = (a, b)
        if vec in plus_dic:
            plus_dic[vec] += 1
        else:
            plus_dic[vec] = 1
    else:
        vec = (a, b)
        if vec in minus_dic:
            minus_dic[vec] += 1
        else:
            minus_dic[vec] = 1


# print(plus_dic, minus_dic, fish_count)

for k, vp in plus_dic.items():
    x, y = k
    if (y, -x) in minus_dic:
        vm = minus_dic[(y, -x)]
        ans = ans * (pow(2, vp, mod) + pow(2, vm, mod) - 1) % mod
        fish_count -= (vp + vm)

ans = ans * pow(2, fish_count, mod) % mod

print((ans - 1 + zero_count) % mod)
