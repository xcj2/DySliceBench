###==================================================
### import
import sys
### stdin
def input(): return sys.stdin.readline()
def iIn(): return int(input())
def iInM(): return map(int, input().split())
def iInLH(): return list(map(int, input().split()))
### setting
sys.setrecursionlimit(10 ** 6)
###---------------------------------------------------

N, M, K = iInM()
A = iInLH()
B = iInLH()

id_a = -1
t_pre = 0
for i in range(N):
    if t_pre + A[i] <= K: ## read
        id_a += 1
        t_pre += A[i]
    else:
        break

id_b = -1
for j in range(M):
    if t_pre + B[j] <= K: ## read
        id_b += 1
        t_pre += B[j]
    else:
        break

ans = (id_a + 1) + (id_b + 1)
if id_a < 0:
    print(ans)
    exit()

while (id_a >= 0):
    t_pre -= A[id_a]
    id_a -= 1
    for j in range(id_b+1, M):
        if t_pre + B[j] <= K:
            id_b += 1
            t_pre += B[j]
        else:
            break
    if ans < (id_a + 1) + (id_b + 1):
        ans = (id_a + 1) + (id_b + 1)
    #print(id_a, id_b)


print(ans)




