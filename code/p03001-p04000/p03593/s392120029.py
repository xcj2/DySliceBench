import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import defaultdict

def judge(cnts, h, w):
    odd_cnt = 0
    mod4_2_cnt = 0
    mod4_0_cnt = 0

    for key, val in cnts.items():
        if val % 2 == 1:
            odd_cnt += 1

        elif val % 4 == 2:
            mod4_2_cnt += 1

        else:
            mod4_0_cnt += 1


    if h == 1 and w == 1:
        return True

    elif h == 1:
        if w % 2 == 1:
            return True if odd_cnt == 1 else False
        else:
            return True if odd_cnt == 0 else False

    elif w == 1:
        if h % 2 == 1:
            return True if odd_cnt == 1 else False
        else:
            return True if odd_cnt == 0 else False

    elif h % 2 == 1 and w % 2 == 1:
        return True if mod4_2_cnt == (w//2 + h//2) and odd_cnt == 1 else False

    elif h%2 == 1:
        return True if mod4_2_cnt == (w//2) and odd_cnt == 0 else False

    elif w%2 == 1:
        return True if mod4_2_cnt == (h//2) and odd_cnt == 0 else False

    else:
        return True if mod4_2_cnt == 0 and odd_cnt == 0 else False


h, w = li()
a = [ns() for _ in range(h)]

char_cnt = defaultdict(int)

for ai in a:
    for aij in ai:
        char_cnt[aij] += 1

print("Yes" if judge(char_cnt, h, w) else "No")