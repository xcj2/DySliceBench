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
    n=inp()
    t=[[] for _ in range(n)]
    s=[[] for _ in range(n)]
    for i in range(n):
        a=inp()
        for _ in range(a):
            x,y=inpm()
            if y==1:
                t[i].append(x-1)
            else:
                s[i].append(x-1)
    res=0
    for k in range(pow(2,n),-1,-1):
        flag = True
        cnt = 0
        for i in range(n):
            if (k>>i)&1 == 1:
                for e in t[i]:
                    if (k>>e)&1 == 0:
                        flag = False
                for e in s[i]:
                    if (k>>e)&1 == 1:
                        flag = False
                cnt+=1
        if flag:
            res = max(res,cnt)
    print(res)


if __name__ == "__main__":
    main()