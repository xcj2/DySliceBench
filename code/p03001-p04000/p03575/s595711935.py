import math,heapq,collections,sys,numpy as np
sys.setrecursionlimit(10**7)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def is_connected(npmat):
    mat = np.copy(npmat)
    dim = mat.shape[0]
    for i in range(dim):
        mat[i][i] = 0
    accessible = set([0])
    queue = [0]
    while len(queue) > 0:
        i = queue.pop()
        js = filter(lambda x:x[1], enumerate(mat[i] > 0))
        for j, bool in js:
            if not j in accessible:
                accessible.add(j)
                if len(accessible) == dim :
                    return True
                queue.append(j)
    return len(accessible) == dim

N,M = LI()
ma = [[0]*N for _ in range(N)]
Ms = []

for _ in range(M):
    a,b = LI_()
    ma[a][b] = 1
    ma[b][a] = 1
    Ms.append((a,b))

ans = 0
for m in Ms:
    ma[m[0]][m[1]] = 0
    ma[m[1]][m[0]] = 0
    if not is_connected(np.array(ma)):
        ans += 1
    ma[m[0]][m[1]] = 1
    ma[m[1]][m[0]] = 1
    
print(ans)
