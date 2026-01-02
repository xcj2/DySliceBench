import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = MI()
P = LI()
C = LI()
loops = []
C_loop = []
for i in range(N):
    j = i
    loops.append([i])
    C_loop.append([0])

    while (P[i] - 1) != j:
        i = P[i] - 1
        C_loop[-1].append(C_loop[-1][-1] + C[i])
        loops[-1].append(i)

    C_loop[-1].append(C_loop[-1][-1] + C[P[i] - 1])


ans_list = [0] * N

for i in range(N):
    if K <= len(loops[i]):
        ans_list[i] = max(C_loop[i][j] for j in range(1, K + 1))
    else:
        if C_loop[i][-1] <= 0:
            ans_list[i] = max(C_loop[i])
        else:
            a = K // len(loops[i])
            ans_list[i] = max(a * C_loop[i][-1] + max(C_loop[i][j] for j in range(K % len(loops[i]) + 1)), (a - 1) * C_loop[i][-1] + max(C_loop[i]))

print(max(ans_list))
