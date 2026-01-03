import queue,sys,collections,math,random;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,M = Is()
mat = [[] for _ in range(N) ]
for _ in range(M):
    a,b = Is()
    a,b = a-1, b-1
    mat[a].append(b)
    mat[b].append(a)

c = 0
def dfs(visited,now):
    if len(visited) == N:
        global c
        c += 1
    else:
        q = mat[now]
        for e in q:
            if not e in visited:
                dfs(visited+[e],e)
dfs([0],0)
print(c)
