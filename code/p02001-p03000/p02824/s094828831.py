def examA():
    N, A, B = LI()
    ans = inf
    if abs(A-B)%2==0:
        ans = abs(A-B)//2
    cur = min((A+B-1)//2,(2*N-A-B+1)//2)
    ans = min(ans,cur)
    print(ans)
    return

def examB():
    N, M, V, P = LI()
    A = LI(); A.sort()
    maxA = A[N-P]
    sumA = maxA*(N-P)-sum(A[:N-P])
#    print(maxA,sumA)
    l = -1; r = N-P
    while(r-l>1):
        flag = True
        now = (l+r)//2
        c = sumA - (maxA-A[now])
        need = maxA - A[now]
        if need>M:
            flag = False
        q = 0
        for i in range(N):
            if A[i]>=maxA-M+(M-need):
                break
            if i==now:
                break
            q +=maxA-M+(M-need)-A[i]
        if (V-P)*M-(N-P)*(M-need)+q>c:
            flag = False
        if flag:
            r = now
        else:
            l = now
#        print(A[now],c,(V-P)*M-(N-P)*(M-need)+q,q,need)
    ans = N-r
    print(ans)
    return

def examC():
    N = I()
    ans = [["."]*N for _ in range(N)]
    if N%3!=0 and N%2!=0:
        print("-1")
        return
    if N%3==0:
        for i in range(N//3):
            ans[i*3][i*3] = "a"
            ans[i*3][i*3+1] = "a"
        for i in range(N//3):
            ans[i*3+1][i*3+2] = "a"
            ans[i*3+2][i*3+2] = "a"
    else:
        for i in range(N//2):
            for j in range((N+2) // 4):
                ans[i * 2][j * 4] = "a"
                ans[i * 2][j * 4 + 1] = "a"
                ans[i * 2 + 1][j * 4] = "b"
                ans[i * 2 + 1][j * 4 + 1] = "b"
                if j*4+2==N:
                    break
                ans[i * 2][j * 4+2] = "c"
                ans[i * 2][j * 4+3] = "c"
                ans[i * 2 + 1][j * 4 + 2] = "d"
                ans[i * 2 + 1][j * 4 + 3] = "d"
            ans[i*2][i*2] = "e"
            ans[i*2+1][i*2] = "e"
            ans[i*2][i*2+1] = "f"
            ans[i*2+1][i*2+1] = "f"
    for v in ans:
        print("".join(map(str,v)))
    return

def examD():
    return

def examE():
    return

def examF():
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
inf = float('inf')

if __name__ == '__main__':
    examB()


"""
                for j in range(N // 4):
                    ans[i * 2][j * 4+2] = "a"
                    ans[i * 2][j * 4 +3] = "a"
                    ans[i * 2 +1][j * 4+2] = "b"
                    ans[i * 2 +1][j * 4 +3] = "b"
                for j in range(N // 4):
                    ans[i*2-2][j*4+2] = "c"
                    ans[i*2-1][j*4+2] = "c"
                    ans[i*2-2][j*4 +3] = "d"
                    ans[i*2-1][j*4 +3] = "d"

"""