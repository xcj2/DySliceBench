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
    B = LIST()
    rest = 0
    count = 0
    for i in range(N):
        if A[i] <= rest:
            count += A[i]
            tmp = 0
        else:
            count += rest
            tmp = A[i] - rest
        if tmp <= B[i]:
            count += tmp
            rest = B[i] - tmp
        else:
            count += B[i]
            rest = 0
    if A[-1] <= rest:
        count += A[-1]
    else:
        count += rest
    print(count)

if __name__ == '__main__':
    main()
