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

from math import floor

def solve():
    a, b = MI()

    for i in range(10000):
        x = floor(i * 0.08)
        y = floor(i * 0.1)
        if x == a and y == b:
            print(i)
            return
    print(-1)


if __name__ == '__main__':
    solve()
