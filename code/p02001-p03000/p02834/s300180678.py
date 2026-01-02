import sys
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline()[:-1]
N,u,v = map(int,input().split(' '))
l = [None]*N
for i in range(N-1):
    l[i] = list(map(int, input().split()))

MAP = {}
for i in range(N):
    if l[i]==None:
        continue
    a,b = l[i]
    if a in MAP:
        MAP[a].append(b)
    else:
        MAP[a] = [b]
    if b in MAP:
        MAP[b].append(a)
    else:
        MAP[b] = [a]

#Tがたどり着くのにかかる手数
t_MAP = [0]*(N+1)
cost = 0

def t_dfs(n,c):
    t_MAP[n] = c
    c += 1
    if n in MAP:
        for j in MAP[n]:
            if t_MAP[j]==0 and j!=u:
                t_dfs(j,c)
t_dfs(u,cost)

a_visited = [False]*(N+1)
break_even = False
pre_tcost = 10**5
ANS = [0]
def a_dfs(n,c,pre_c):
    a_visited[n] = True
    t_cost = t_MAP[n]
    if t_cost>c:
        if t_cost>pre_c:
            return
    ANS[0] = max(c,ANS[0])
    c += 1
    if n in MAP:
        for j in MAP[n]:
            if not a_visited[j]:
                a_dfs(j,c,t_cost)
a_visited[v] = True
a_dfs(v,cost,pre_tcost)
print(ANS[0]-1)
