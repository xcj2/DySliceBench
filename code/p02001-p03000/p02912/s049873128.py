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
import heapq

def main():
    N, M = MAP()
    A = [-int(i) for i in input().split()]
    heapq.heapify(A)
    for mm in range(M):
        minv = heapq.heappop(A)
        heapq.heappush(A, minv / 2)
    print(sum([int(x) for x in A]) * -1)


if __name__ == '__main__':
    main()
