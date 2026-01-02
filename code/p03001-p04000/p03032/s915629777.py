from collections import Counter,defaultdict,deque
import sys
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
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
    n,k = inpm()
    v = inpl()
    a = [0 for _ in range(n+1)]
    b = [0 for _ in range(n+1)]
    ans = 0
    for i in range(n):
        a[i+1] = a[i] + v[i]
        b[i+1] = b[i] + v[n-1-i]
    for x in range(min(n+1,k+1)):
        for y in range(min(n-x+1,k-x+1)):
            que = []
            for i in range(x):
                que.append(v[i])
            for i in range(y):
                que.append(v[n-1-i])
            que.sort()
            l = len(que)
            pre = a[x] + b[y]
            for z in range(min(l,k-x-y)):
                if que[z]>=0:
                    break
                pre -= que[z]
                ans = max(ans,pre)
            ans = max(ans,pre)
    print(ans)

if __name__ == "__main__":
    main()