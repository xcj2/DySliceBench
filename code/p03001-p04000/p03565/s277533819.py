def examC():
    St = S(); T = S()
    N = len(St) - len(T)
    ans = -1
    for i in range(N,-1,-1):
        cur = 0
        for j in range(len(T)):
            if St[i+j]=="?" or St[i+j]==T[j]:
                cur +=1
                continue
            else:
                break
        if cur==len(T):
            ans =i
            break
    if ans == -1:
        ans="UNRESTORABLE"
    else:
        newS = ""
        for i in range(ans):
            if St[i]=="?":
                newS +="a"
            else:
                newS +=St[i]
        for i in range(ans,ans+len(T)):
            newS += T[i-ans]
        for i in range(ans+len(T),len(St)):
            if St[i]=="?":
                newS +="a"
            else:
                newS +=St[i]
        ans = newS
    print(ans)


import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
