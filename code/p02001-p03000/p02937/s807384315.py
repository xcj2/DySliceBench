import sys
from collections import defaultdict
import bisect
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return sys.stdin.readline()[:-1]

def main():
    s = list(S())
    t = list(S())

    alfa = defaultdict(list)
    for i, c in enumerate(s):
        alfa[c].append(i)
    pre = -1
    ans = 0
    for i, c in enumerate(t):
        index = alfa[c]
        if len(index) == 0:
            print(-1)
            return
        a = bisect.bisect_right(index, pre)
        if a != len(index):
            pre = index[a]
        else:
            pre = index[0]
            ans += len(s)

    print(ans + pre + 1)
if __name__ == '__main__':
    main()