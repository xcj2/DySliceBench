def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
import math

N = INT()
A = LIST()


if (N == 0 and A[0] != 1) or (N > 0 and A[0] != 0):
    print(-1)
    exit()


node_min, node_max = [0]*(N+1), [0]*(N+1)
node_min[-1] = A[-1]
node_max[-1] = A[-1]
for i in reversed(range(N)):
    node_min[i] = math.ceil(node_min[i+1]/2) + A[i]
    node_max[i] = node_max[i+1] + A[i]


if node_min[0] > 1:
    print(-1)
    exit()

ans = 1
node = 1
for i in range(1, N+1):
    node = min(node_max[i], 2*node)
    ans += node
    node = node - A[i]


print(ans)





