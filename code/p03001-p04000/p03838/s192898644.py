def examA():
    x, y = LI()
    ans = 0
    if x<0 and y<0:
        if x<=y:
            ans = y-x
        else:
            ans = x-y+2
    elif x<0 and 0<=y:
        if -x<=y:
            ans = y+x+1
        else:
            ans = min(-(x+y)+1,y-x)
    elif y<=0:
        ans = abs(y+x)+1
    else:
        if x<=y:
            ans = y-x
        else:
            ans = x-y+2
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18

if __name__ == '__main__':
    examA()
