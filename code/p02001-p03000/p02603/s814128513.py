import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
B = [0] + LI()

A = [0,B[1]]
for i in range(1,N):
    if B[i] != B[i+1]:
        A.append(B[i+1])

N = len(A)-1

MAX = [0,1000] + [0]*N

from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(n,money):
    if n == N+1:
        return money
    else:
        res = money
        for i in range(n,N):  # 購入
            for j in range(i+1,N+1):  # 売却
                if A[i] == min(A[i:j+1]) and A[j] == max(A[i:j+1]) and A[i] < A[j]:
                    if money+(A[j]-A[i])*(money//A[i]) > MAX[j+1]:
                        res = max(res,dfs(j+1,money+(A[j]-A[i])*(money//A[i])))
                        MAX[j+1] = money+(A[j]-A[i])*(money//A[i])
        return res

print(dfs(1,1000))
