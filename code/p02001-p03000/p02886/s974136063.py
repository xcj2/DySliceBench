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

def printlist(lst, k='\n'): return k.join(list(map(str, lst)))
INF = float('inf')

from itertools import combinations


def solve():
    n = II()
    D = LI()

    ans = 0
    for i in combinations(D, 2):
        # print(i)
        x, y = i
        ans += x * y
    print(ans)

if __name__ == '__main__':
    solve()
