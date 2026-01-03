def examA():
    S = SI()
    ans = "No"
    flag = False
    for s in S:
        if flag:
            if s=="F":
                ans = "Yes"
                break
        else:
            if s=="C":
                flag = True
    print(ans)
    return

def examB():
    K, T = LI()
    A = LI(); A.sort()
    ans = max(0,A[-1]*2-sum(A)-1)
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
    examB()
