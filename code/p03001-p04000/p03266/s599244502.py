import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')
from math import ceil

def solve():
    N, K = MI()

    NmodK = N % K if N % K != 0 else K
    times = ceil(N / K)
    ans = 0
    for a in range(1, K+1):
        b = K - a if K - a > 0 else K
        c = b
        # print(a, b, c)
        if (b + c) % K == 0:
            cnt_b = (N - b) // K + 1
            # print('bbb', cnt_b)
            if a <= NmodK:
                t = times
            else:
                t = times - 1
            # print(cnt_b ** 2, t)
            ans += cnt_b ** 2 * t
    print(ans)



if __name__ == '__main__':
    solve()
