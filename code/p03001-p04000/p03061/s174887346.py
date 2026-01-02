import sys
import math
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MAT(h): return [list(map(int, input().split())) for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = INT()
    A = LIST()
    L = [0] * N
    R = [0] * N
    M = [0] * N
    for i in range(N - 1):
        L[i + 1] = gcd(L[i], A[i])
        R[N - i - 2] = gcd(R[N - i - 1], A[N - i - 1])
    maxv = 0
    for i in range(N):
        M[i] = gcd(L[i], R[i])
        if maxv < M[i]:
            maxv = M[i]
    print(maxv)

if __name__ == '__main__':
    main()
