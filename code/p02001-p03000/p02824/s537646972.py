from collections import Counter,defaultdict,deque
import sys
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# mod = 10**9+7
    
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
    n,m,v,p = inpm()
    a = inpl()
    a.sort(reverse=True)
    ok = 0
    ng = n
    while ng-ok >1:
        mid = (ok+ng)//2
        if mid+1 <= p:
            ok = mid
        elif a[p-1] > a[mid]+m:
            ng = mid
        else:
            key = 0
            cnt = (p)*m + (n-mid-1)*m
            for i in range(mid-1,p-2,-1):
                if a[i] > a[mid]+m:
                    ng = mid
                    key = 1
                    break
                cnt += min(a[mid]-a[i]+m,m)
            if key:
                break
            if cnt >= m*v:
                ok = mid
            else:
                ng = mid
    print(ok+1)

if __name__ == "__main__":
    main()