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

def main():
    L, R = MAP()
    LL = L % 2019
    RR = R % 2019
    if (R - L) >= 2019:
        print(0)
    else:
        minv = 2019
        for l in range(LL, RR):
            for r in range(l + 1, RR + 1):
                minv = min(minv, (l * r) % 2019)
        print(minv)

if __name__ == '__main__':
    main()
