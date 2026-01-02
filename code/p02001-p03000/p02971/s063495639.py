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
    maxv = 0
    maxv2 = 0
    A = [INT() for i in range(N)]
    A_ = sorted(A, reverse = True)
    maxv = A_[0]
    maxv2 = A_[1]
    for i in range(N):
        if A[i] == maxv:
            print(maxv2)
        else:
            print(maxv)

if __name__ == '__main__':
    main()
