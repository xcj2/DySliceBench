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
    N = INT()
    A = LIST()
    x = [0] * N
    sumx = sum(A)
    x[0] = sumx - sum(A[1::2]) * 2
    for i in range(1, N):
        x[i] = A[i - 1] * 2 - x[i - 1]
    print(*x)

if __name__ == '__main__':
    main()
