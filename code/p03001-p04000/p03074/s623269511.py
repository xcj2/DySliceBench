import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def POW(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return POW(x, y // 2) ** 2 % MOD
    else:
        return POW(x, y // 2) ** 2 * x % MOD
def mod_factorial(x, y): return x * POW(y, MOD - 2) % MOD
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import Counter
from itertools import accumulate

def main():
    N, K = LI()
    S = SI()
    cnts = []
    pre = '1'
    cnt = 0
    # 0 start bin
    for s in S:
        if s != pre:
            cnts.append(cnt)
            cnt = 0
            pre = s
        cnt += 1
    cnts.append(cnt)
    acc = [0] + list(accumulate(cnts))
    ans = 0
    for i in range(0, len(acc) - 1, 2):
        tmp = acc[min(len(acc) - 1, i + 2 * K + 1)] - acc[i]
        ans = max(tmp, ans)
        if len(acc) < i + 2 * K + 1:
            break

    return ans

print(main())