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

import heapq

def solve():
    n, m = MI()
    A = LI()

    A = list(map(lambda x: -x, A))

    heapq.heapify(A)
    # print(A)

    for i in range(m):
        x = heapq.heappop(A)
        heapq.heappush(A, x / 2)

    A = list(map(lambda x: int(-x), A))
    print(sum(A))
if __name__ == '__main__':
    solve()
