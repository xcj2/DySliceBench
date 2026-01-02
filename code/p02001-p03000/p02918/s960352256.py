import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


# A
def A():
    N = I()
    print(pow(N, 3))
    return


# B
def B():
    N = I()
    A = LI()
    B = LI()
    C = LI()
    a_p = -1
    ans = 0
    for a in A:
        if (a - a_p == 1):
            ans += B[a - 1] + C[a - 2]
        else:
            ans += B[a - 1]
        a_p = a
    print(ans)
    return


# C
def C():
    N = I()
    B = LI()
    A = [0 for i in range(N)]
    A[0] = B[0]
    A[N - 1] = B[N - 2]
    for i in range(1, N - 1):
        A[i] = min(B[i - 1], B[i])
    print(sum(A))
    return


# D
def D():
    n,k=LI()
    s=S()
    cnt1=0
    cnt2=0
    i_pre=''
    if(s[0]=='L'):
        cnt1+=1
    if(s[n-1]=='R'):
        cnt1+=1
    for i in s:
        if i_pre=='R' and i=='L':
            cnt2+=1
        i_pre=i
    ans=n-cnt1-2*cnt2
    if cnt1==0:
        if k<=cnt2-1:
            print(ans+2*k)
        else:
            print(n-1)
    if cnt1==1:
        if k<=cnt2:
            print(ans+2*k)
        else:
            print(n-1)
    if cnt1==2:
        if k<=cnt2:
            print(ans+2*k)
        else:
            print(n-1)
    return


# E
def E():
    return


# F
def F():
    return


# Unittest
def resolve():
    D()
    return


# Solve
if __name__ == "__main__":
    D()
