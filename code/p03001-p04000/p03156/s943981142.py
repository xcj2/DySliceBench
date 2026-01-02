def examB():
    N = I(); A,B = LI()
    P = LI()
    exam = [0]*3
    for i in P:
        if i<=A:
            exam[0] +=1
        elif i<=B:
            exam[1] +=1
        else:
            exam[2] +=1
    ans = min(exam)
    print(ans)

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