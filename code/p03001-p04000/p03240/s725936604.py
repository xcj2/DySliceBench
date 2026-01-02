def examA():
    N = I()
    if N==1:
        ans = "Hello World"
    elif N==2:
        A = I(); B = I()
        ans = A + B
    try:
        print(ans)
    except:
        print()
    return

def examB():
    N, T = LI()
    ans =  10**9
    for _ in range(N):
        c, t = LI()
        if T>=t and ans>c:
            ans = c
    if ans==10**9:
        ans = "TLE"
    print(ans)
    return

def examC():
    N = I()
    X, Y, H = [0]*N, [0]*N, [0]*N
    for i in range(N):
        X[i], Y[i], H[i] = LI()
    for x in range(101):
        for y in range(101):
            curH = 0; flag = True; keep = []
            for i in range(N):
                if H[i]==0:
                    keep.append(i)
                    continue
                now = H[i] + abs(x-X[i]) + abs(y-Y[i])
                if curH==0:
                    curH = now
                else:
                    if curH!=now:
                        flag = False
                        break
            for i in keep:
                now = abs(x-X[i]) + abs(y-Y[i])
                if now<curH:
                    flag = False
                    break
            if flag:
                ans = [x,y,curH]
                break
    print(" ".join(map(str,ans)))
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
