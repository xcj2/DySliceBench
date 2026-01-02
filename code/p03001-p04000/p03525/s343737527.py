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
    a=inpl()
    a.sort()
    dic = defaultdict(int)
    dic[0] += 1
    for i in range(n):
        dic[a[i]] += 1
    for e in dic:
        if dic[e] > 2:
            print(0)
            return
        if e == 0 or e == 12:
            if dic[e]>1:
                print(0)
                return
    x = [0 for _ in range(24)]
    cnt = 0
    for i in range(13):
        if dic[i]==0:
            continue
        elif dic[i] == 1:
            if cnt % 2 == 0:
                x[i] += 1
            else:
                x[24-i] += 1
        else:
            x[i] += 1
            x[24-i] += 1
        cnt += 1
    ans = 24
    for i in range(24):
        for j in range(24):
            if i==j or x[i]==0 or x[j]==0:
                continue
            ans = min(ans,abs(i-j),24-abs(i-j))
    print(ans)

if __name__ == "__main__":
    main()