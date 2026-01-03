import sys
stdin = sys.stdin

from itertools import accumulate

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, w = li()
value = {i: [] for i in range(4)}

for i in range(n):
    wei, val = li()

    if i == 0:
        w0 = wei

    value[wei - w0].append(val)

for i in range(4):
    value[i].sort(reverse=True)

    value[i] = [0] + list(accumulate(value[i]))


ans = 0

for i in range(len(value[0])):
    for j in range(len(value[1])):
        for k in range(len(value[2])):
            rest = w - i*w0 - j*(w0+1) - k*(w0+2)
            x = rest // (w0+3)

            if x < 0:
                continue
            else:
                ans = max(ans, value[0][i] + value[1][j] + value[2][k] + value[3][min(len(value[3])-1, x)])

print(ans)
