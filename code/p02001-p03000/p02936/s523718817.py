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
    N, Q = MAP()
    AB = sorted(MATINT(N-1))
    plus = [0] * N
    ans = [0] * N
    for i in range(Q):
        P, X = MAP()
        plus[P-1] += X
    for ab in AB:
        plus[ab[1]-1] += plus[ab[0]-1]
    print(*plus)

if __name__ == '__main__':
    main()
