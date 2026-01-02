import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
B = [0] + LI()

A = [0]
for i in range(N):  # 要らないものを消す
    if B[i] != B[i+1]:
        A.append(B[i+1])

N = len(A)-1
MAX = [0,1000] + [0]*N  # MAX[i] = i日目開始時点の所持金の最大値

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
                    a = money+(A[j]-A[i])*(money//A[i])
                    if a > MAX[j+1]:
                        res = max(res,dfs(j+1,a))
                        MAX[j+1] = a
        return res

print(dfs(1,1000))
