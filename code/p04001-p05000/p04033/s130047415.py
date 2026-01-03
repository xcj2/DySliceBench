def examA():
    a, b = LI()
    if a>0:
        ans = "Positive"
        print(ans)
        return
    if b>=0:
        ans = "Zero"
    else:
        judge = b-a
        if judge%2==1:
            ans = "Positive"
        else:
            ans = "Negative"
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
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examA()
