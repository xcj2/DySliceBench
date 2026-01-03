def BFS(N,start,roots):
    dist = [-1] * N
    stack = []
    stack.append(start)
    dist[start] = 0
    while stack:
        label = stack.pop(-1)
        for i, c in roots[label]:
            if dist[i] == -1:
                dist[i] = dist[label] + c
                stack += [i]
    return dist
############################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N = I()
v = [[] for i in range(N)]
for i in range(N-1):
    a, b, c = LI()
    v[a-1].append([b-1,c])
    v[b-1].append([a-1,c])
Q, K =LI()

#print(BFS(N,K-1,v))
W = BFS(N,K-1,v)
ansC = []
for i in range(Q):
    x, y = LI()
    ansC.append(W[x-1]+W[y-1])

for v in ansC:
    print(v)