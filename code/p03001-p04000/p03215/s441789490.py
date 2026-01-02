def examA():
    N = I(); A = LI()
    sumnale = sum(A)/N
    cur = 10**9; curL = 0
    for i in range(N):
        if cur>abs(A[i]-sumnale):
            cur = abs(A[i]-sumnale)
            curL = i
    ans = curL
    print(ans)
    return

def examB():
    N, K = LI(); A = LI()
    AK = []; ans = 0
    d = defaultdict(int)
    for i in range(N):
        cur = A[i]
        AK.append(cur)
        for k in range(40):
            if cur&(1<<k)==(1<<k):
                d[k] +=1
        for j in range(i+1,N):
            cur += A[j]
            AK.append(cur)
            for k in range(40):
                if cur & (1 << k) == (1 << k):
                    d[k] += 1
#    print(AK)
#    print(d)
    k = 40; curA = []
    while(k>0):
        k -=1
        if d[k]<K:
            continue
        for i in range(len(AK)):
            if AK[i]&(1<<k)==(1<<k):
                curA.append(AK[i])
        if len(curA)>=K:
            ans = 2**k
            break
#    print(curA)
    while(k>0):
        k -=1; neA = []
        if d[k]<K:
            continue
        for i in range(len(curA)):
            if curA[i]&(1<<k)==(1<<k):
                neA.append(curA[i])
        if len(neA)<K:
            continue
        else:
            curA = copy.deepcopy(neA)
            ans += 2**k
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
