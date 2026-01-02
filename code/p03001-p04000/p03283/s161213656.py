from collections import Counter,defaultdict,deque
import sys
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
    
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])


def main():
    n,m,Q = inpm()
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        l,r = inpm()
        r-=1
        ans[r][0]+=1
        if l != n:
            ans[r][l] -= 1
    for i in range(n):
        for j in range(1,n):
            ans[i][j] += ans[i][j-1]
    for i in range(n):
        for j in range(1,n):
            ans[j][i] += ans[j-1][i]
    for _ in range(Q):
        p,q = inpm()
        print(ans[q-1][p-1])

if __name__ == "__main__":
    main()