import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    N = i_input()
    N = math.factorial(N)

    def prime_decomposition(n):
        i = 2
        table = []
        while i * i <= n: # sqrt(n)で計算が済む
            while n % i == 0:
                n //= i
                table.append(i)
            i += 1
        if n > 1:
            table.append(n)
        return table

    N = sorted(prime_decomposition(N))
    ans = 1
    for i,k in itertools.groupby(N):
        ans *= len(list(k)) + 1
    print(ans%MOD)



if __name__=="__main__":
    main()
