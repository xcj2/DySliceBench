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

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import ceil

def solve():
    n, a, b = MI()
    # a -= 1
    # b -= 1

    left = max(a-1, b-1)
    right = max(n-a, n-b)

    center = INF
    sa = abs(b - a)
    if a % 2 == b % 2:
        center = sa // 2
    else:
        t = min(a-1, n-b)
        center = t + (sa-1) // 2 + 1
    # print(left, right, center)
    print(min([left, right, center]))


if __name__ == '__main__':
    solve()
