import sys
sys.setrecursionlimit(10**7)

debug = True
#debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

mx = 10**9 + 7

from math import factorial
# def npr(n, r):
#     ans = math.factorial(n+r) // (math.factorial(n) * math.factorial(r))
#     return ans

def ncr(n, r):
    a = factorial(n) // (factorial(r) * factorial(n - r))
    return a

def solve():
    N, K = map(int, input().split())
    M = N - K

    for i in range(1, K+1):
        if M+1 < i:
            print(0)
            continue
        # まず、赤がM個あるので、両端を含む隙間 M+1 から、i個選ぶ
        agroup = ncr(M+1, i)

        # そのあと、青iこの箱にKをを分ける
        bagroup = ncr(K-1, i-1)

        print((agroup * bagroup) % mx)

solve()