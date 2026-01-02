def examC():
    N = I(); D = LI()
    ans = -1
    choice = [0]*13; choice[0] +=1
    for i in D:
        choice[i] +=1
        if choice[i]>2:
            ans = 0
            break
    if choice[0]>=2 or choice[12]>=2:
        ans = 0
#    print(choice)
    curT = [0]; cur = []
    for i in range(1,12):
        if choice[i]==1:
            cur.append(i)
        elif choice[i]==2:
            curT.append(i)
            curT.append(24-i)
    ne = Counter(choice)
    if choice[12]==1:
        ne[1] -=1
        curT.append(12)
    loop = 2**(ne[1]-1)
#    print(loop)
    if ans==0:
        print(ans)
        exit()
    ans = 0
    for i in range(loop):
        now = copy.deepcopy(curT); ansC = 24
        for j in range(ne[1]-1):
            if i&(1<<j)==(1<<j):
                now.append(cur[j])
            else:
                now.append(24-cur[j])
        now.sort()
        for k in range(len(now)):
            if k != len(now) - 1:
                ansC = min(ansC, now[k+1]-now[k], 24-(now[k+1]-now[k]))
            else:
                ansC = min(ansC, now[k], 24-now[k])
        ans = max(ans, ansC)
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
    examC()
