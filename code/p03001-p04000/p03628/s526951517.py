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
    n=inp()
    s1=input()
    s2=input()
    if s1[0]==s2[0]:
        ans=3
        index=1
        key=0
    else:
        ans=6
        index=2
        key=1
    while index<=n-1:
        if s1[index]==s2[index]:
            if key==0:
                ans=(ans*2)%mod
                index+=1
            else:
                key=0
                index+=1
                continue
        else:
            if key==0:
                ans=(ans*2)%mod
                index+=2
                key=1
            else:
                ans=(ans*3)%mod
                index+=2
    print(ans)
if __name__ == "__main__":
    main()