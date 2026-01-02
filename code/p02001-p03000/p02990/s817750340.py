import sys, math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

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
    N, K = MAP()
    NK = N - K + 1
    for i in range(K):
        if NK < i + 1:
            print(0)
        else:
            print(combinations_count(NK, i + 1) * combinations_count(K - 1, i) % mod)

if __name__ == '__main__':
    main()
