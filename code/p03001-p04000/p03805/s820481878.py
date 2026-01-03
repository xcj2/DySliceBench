N, M = map(int, input().split())
A = [0]*M
B = [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())

from itertools import permutations

def make_aja_mtx(N, M, A, B):
    D = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        D[A[i]-1][B[i]-1] = 1
        D[B[i]-1][A[i]-1] = 1
    return D

def check(p, N, D):
    len_path = 1
    for i in range(1, N):
        if D[p[i-1]-1][p[i]-1] == 1:
            len_path += 1
        else:
            break
    return len_path == N
        
def perm(perm_2):
    for p in perm_2:
        yield (1,) + p

def Main(N, M, A, B):
    ns = range(2, N+1)
    perm_2 = permutations(ns, N-1)
    ans = 0
    D = make_aja_mtx(N, M, A, B)
    for p in perm(perm_2):
        if check(p, N, D):
            ans += 1
    return ans
    
print(Main(N, M, A, B))
