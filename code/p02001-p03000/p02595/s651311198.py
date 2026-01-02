# import sys
# input = sys.stdin.readline
# import re
import math
import itertools

def main():
    n, d = input_list()
    ans = 0
    for _ in range(n):
        x, y = input_list()
        a = math.sqrt((x * x) + (y * y))
        if a <= d:
            ans += 1
    print(ans)

# 累積和
def get_camulative(l):
    return [0] + list(itertools.accumulate(l))

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def count(mazes, hc, wc):
    hc = list(hc)
    wc = list(wc)
    r = 0
    for hi, row in enumerate(mazes):
        if hi in hc:
            continue
        for wi, m in enumerate(row):
            if wi in wc:
                continue
            if m == '#':
                r += 1
    return r

def input_list():
    return list(map(int, input().split()))

def input_list_str():
    return list(map(str, input().split()))

if __name__ == '__main__':
    main()

