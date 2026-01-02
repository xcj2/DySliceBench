import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

from functools import lru_cache

def main(): 
    N, L = LI()
    # abs_min = INF

    li = []
    for i in range(1, N+1):
        li.append((abs(L+i-1), L+i-1))

    li.sort()
    li.pop(0)

    sum_ = 0
    for i in li:
        sum_ += i[1]

    print(sum_)


main()