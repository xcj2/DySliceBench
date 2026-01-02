def examA():
    S = SI()
    if S=="ARC":
        ans = "ABC"
    else:
        ans = "ARC"
    print(ans)
    return

def examB():
    N, K = LI()
    snuke = set(range(1,N+1))
    for _ in range(K):
        d = I()
        A = LI()
        for a in A:
            snuke.discard(a)
    ans = len(snuke)
    print(ans)
    return

def examC():
    N, M = LI()
    H = LI()
    good = set(range(1,N+1))
    for _ in range(M):
        a, b = LI()
        if H[a-1]>=H[b-1]:
            good.discard(b)
        if H[b-1]>=H[a-1]:
            good.discard(a)
    ans = len(good)
    print(ans)
    return

def examD():
    X = I()
    #print(1000**5-999**5)
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5-b**5==X:
                print(a,b)
                return
    return

def examE():
    N = I()
    A = LI()
    B = [0]*N
    D = defaultdict(int)
    for i in range(N):
        B[i] = A[i]-i
        c = A[i]+i
        D[c] += 1
    #print(B)
    #print(D)
    ans = 0
    for b in B:
        ans += D[-b]
    print(ans)
    return

def examF():
    def Run_Length_Encoding(s):
        tmp, count, res = s[0], 1, []
        for i in range(1, len(s)):
            if tmp == s[i]:
                count += 1
            else:
                res.append((count, tmp))
                tmp = s[i]
                count = 1
        res.append((count, tmp))
        return res

    N, A, B, C = LI()
    S = [SI()for _ in range(N)]
    SS = Run_Length_Encoding(S)
    #print(SS)
    n = len(SS)
    ans = [""]*(N)
    def judge(a,b):
        if a<0 or b<0:
            return False
        return True
    def dfs(i,num,A,B,C):
        if i==n:
            if A>=0 and B>=0 and C>=0:
                print("Yes")
                for v in ans:
                    print(v)
                exit()
            return
        cnt, s = SS[i]
        if s=="AB":
            if A==0 and B==0:
                return
            for j in range(cnt//2 -1):
                if A==0:
                    ans[num] = "A"
                    num += 1
                    ans[num] = "B"
                else:
                    ans[num] = "B"
                    num += 1
                    ans[num] = "A"
            if cnt>=2:
                A += 1; B -= 1
                if judge(A, B):
                    ans[num] = "A"
                    dfs(i + 1, num + 1, A, B, C)
                A -= 2; B += 2
                if judge(A, B):
                    ans[num] = "B"
                    dfs(i + 1, num + 1, A, B, C)
                A += 1;
                B -= 2
            if cnt%2==0:
                dfs(i+1,num+1,A,B,C)
                return
            A += 1; B -= 1
            if judge(A,B):
                ans[num] = "A"
                dfs(i+1,num+1,A,B,C)
            A -= 2; B += 2
            if judge(A,B):
                ans[num] = "B"
                dfs(i+1,num+1,A,B,C)
            A += 1; B -= 2
        elif s=="BC":
            if B==0 and C==0:
                return
            for j in range(cnt//2 -1):
                if B==0:
                    ans[num] = "B"
                    num += 1
                    ans[num] = "C"
                else:
                    ans[num] = "C"
                    num += 1
                    ans[num] = "B"
            if cnt%2==0:

                dfs(i+1,num+1,A,B,C)
                return
            B += 1; C -= 1
            if judge(B,C):
                ans[num] = "B"
                dfs(i+1,num+1,A,B,C)
            B -= 2; C += 2
            if judge(B,C):
                ans[num] = "C"
                dfs(i+1,num+1,A,B,C)
            B += 1; C -= 2
        else:
            if A==0 and C==0:
                return
            for j in range(cnt//2 -1):
                if A==0:
                    ans[num] = "A"
                    num += 1
                    ans[num] = "C"
                else:
                    ans[num] = "C"
                    num += 1
                    ans[num] = "A"
            if cnt%2==0:
                dfs(i+1,num+1,A,B,C)
                return
            A += 1; C -= 1
            if judge(A, C):
                ans[num] = "A"
                dfs(i + 1,num+1,A,B,C)
            A -= 2; C += 2
            if judge(A, C):
                ans[num] = "C"
                dfs(i + 1,num+1,A,B,C)
            A += 1; C -= 2
        return
    dfs(0,0,A,B,C)
    print("No")
    return


def examF2():
    N, A, B, C = LI()
    S = [SI() for _ in range(N)]
    # print(SS)
    ans = [""] * N

    def judge(a, b):
        if a < 0 or b < 0:
            return False
        return True

    def dfs(i, A, B, C):
        if i == N:
            if A >= 0 and B >= 0 and C >= 0:
                print("Yes")
                for v in ans:
                    print(v)
                exit()
            return
        s = S[i]
        if s == "AB":
            if A == 0 and B == 0:
                return
            A += 1;
            B -= 1
            if judge(A, B):
                ans[i] = "A"
                dfs(i + 1, A, B, C)
            A -= 2;
            B += 2
            if judge(A, B):
                ans[i] = "B"
                dfs(i + 1, A, B, C)
            A += 1;
            B -= 1
        elif s == "BC":
            if B == 0 and C == 0:
                return
            B += 1;
            C -= 1
            if judge(B, C):
                ans[i] = "B"
                dfs(i + 1, A, B, C)
            B -= 2;
            C += 2
            if judge(B, C):
                ans[i] = "C"
                dfs(i + 1,A, B, C)
            B += 1;
            C -= 1
        else:
            if A == 0 and C == 0:
                return
            A += 1;
            C -= 1
            if judge(A, C):
                ans[i] = "A"
                dfs(i + 1, A, B, C)
            A -= 2;
            C += 2
            if judge(A, C):
                ans[i] = "C"
                dfs(i + 1, A, B, C)
            A += 1;
            C -= 1
        return

    dfs(0, A, B, C)
    print("No")
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF2()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""