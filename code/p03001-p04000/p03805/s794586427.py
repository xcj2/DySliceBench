import sys
import copy

sys.setrecursionlimit(1000)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def LIST(): return [int(x) for x in input().split()]
MOD = 10**9 + 7

N, M = LIST()

A = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = LIST()
    A[a][b] = A[b][a] = 1



def check(current, tovisit):
    if tovisit == []:
        return 1
    
    count = 0

    for i in tovisit:
        if A[current][i] == 1:
            tmp = copy.deepcopy(tovisit)
            tmp.remove(i)
            count += check(i, tmp)

    return count

print(check(1, list(range(2, N+1))))
