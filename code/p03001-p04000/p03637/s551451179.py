
def examC():
    N = I()
    A = LI()
    multi2 = 0; multi4 = 0
    for i in A:
        if i%4==0:
            multi4 +=1
        elif i%2==0:
            multi2 +=1
    if multi4>=(N//2):
        ans = "Yes"
    elif (multi4*2 + multi2)>=N:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)



import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
