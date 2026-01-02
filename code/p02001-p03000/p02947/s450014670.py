import sys

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MATINT(h): return [list(map(int, input().split())) for _ in range(h)]
def MATSTR(h): return [input() for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
inf = float('inf')
mod = 10 ** 9 + 7
from collections import Counter

def main():
    N = INT()
    S = []
    for _ in range(N):
        tmp = Counter(input())
        S_tmp = ''
        for i in sorted(tmp.keys()):
            S_tmp += i + str(tmp[i])
        S.append(S_tmp)
    # alpha2num = lambda c: ord(c) - ord('a')
    count = Counter(S)
    ans = 0
    for i in count.values():
        if i > 1:
            ans += i * (i - 1) / 2
    print(int(ans))

if __name__ == '__main__':
    main()
