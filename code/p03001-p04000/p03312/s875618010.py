def examC():
    N = I()
    A = LI()
    Ad = [0]*N
    for i in range(N):
        Ad[i] = A[i]-(i+1)
    Ad.sort()
#    print(Ad)
    b = Ad[N//2]
    ans = 0
    for a in Ad:
        ans +=abs(a-b)
    print(ans)
    return

def examD():
    N = I()
    A = LI()
    cumA = [0]*N
    cumA[0] = A[0]
    for i in range(N-1):
        cumA[i+1] = cumA[i]+A[i+1]
    ans = inf
#    print(cumA)
    for i in range(1,N-1):
        curcd = (cumA[i]+1)//2
        cd = bisect.bisect_right(cumA,curcd)
#        print(curcd,cd)
        C = cumA[cd]; D = cumA[i]-C
        if cd>0 and abs(C-D)>abs(cumA[cd-1]-(cumA[i]-cumA[cd-1])):
            C = cumA[cd-1]; D = cumA[i] - C
        curef = (cumA[-1]-cumA[i]+1)//2
        ef = bisect.bisect_right(cumA,curef+cumA[i])
#        print(curef,ef)
        E = cumA[ef]-cumA[i]; F = cumA[-1]-E-cumA[i]
        if abs(E-F)>abs(cumA[ef-1]-cumA[i]-(cumA[-1]-cumA[ef-1])):
            E = cumA[ef-1]-cumA[i]; F = cumA[-1]-E-cumA[i]
 #           print(E,F)
        ansC = max(C,D,E,F)-min(C,D,E,F)
        ans = min(ans,ansC)
 #       print(C,D,E,F)
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
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examD()
