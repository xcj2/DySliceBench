import sys
sys.setrecursionlimit(10**7)

def LI(): return [int(x) for x in input().split()]
def TI(): return tuple(LI())
def II(): return int(input())

N,M=LI()

MP={}
for _ in range(M):
    fr, to = TI()
    if not fr in MP:
        MP[fr] = []
    MP[fr].append(to)

RESL=[-1]*(N+1)
def dfs(n):
    if RESL[n] != -1:
        return RESL[n]
    else:
        res = 0
        if n in MP:
            for to in MP[n]:
                res = max(res, dfs(to))
            res += 1
        RESL[n] = res
        return res
for i in range(1, N+1): dfs(i)
# print(RESL)
print(max(RESL))
