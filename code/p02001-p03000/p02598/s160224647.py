import sys
import math
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, K = na()
A_array = na()

min_length = 0
max_length = 2 * 10 ** 9

while(max_length - min_length > 0.01):
    mid = (min_length + max_length) / 2
    cut_cnt = 0
    for a in A_array:
        c = a // mid
        if a - mid * c > 0:
            c += 1
        cut_cnt += (c - 1)
    # print(mid, cut_cnt)
    if cut_cnt <= K:
        max_length = mid
    else:
        min_length = mid

# print(max_length)


ans1 = math.floor(max_length)
ans2 = math.ceil(max_length)

if ans1 == 0:
    print(1)
    exit()

cut_cnt = 0
for a in A_array:
    c = a // ans1
    if a - ans1 * c > 0:
        c += 1
    cut_cnt += (c - 1)

if cut_cnt <= K:
    print(ans1)
else:
    print(ans2)
