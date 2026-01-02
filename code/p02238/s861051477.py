N = int(input())
UK = [list(map(int,input().split())) for _ in range(N)]

class Graph:
    def __init__(self,vertex,edge):
        self.v = vertex
        self.e = edge
        self.v_color = [False for _ in range(N)]

    def color(self,u):
        self.v_color[u-1] = True

    def v_exists(self,u):
        flag = False
        for v in self.v:
            if (u,v) in self.e and self.v_color[v-1] == False:
                flag = True
                break
        return flag

V = [i+1 for i in range(N)]
E = []
for i in range(N):
    for j in range(len(UK[i])-2):
        E.append((i+1,UK[i][j+2]))

g = Graph(V,E)

ts = [[0 for _ in range(2)] for _ in range(N+1)]
time = 0

def dfs(u):
    global time
    time += 1
    g.color(u)
    if ts[u-1][0] == 0:
        ts[u-1][0] = time
    while g.v_exists(u):
        for v in g.v:
            if (u,v) in g.e and g.v_color[v-1] == False:
                dfs(v)
    time += 1
    if ts[u-1][1] == 0:
        ts[u-1][1] = time

for i in range(N):
    if g.v_color[i] == False:
        dfs(i+1)

for i in range(N):
    print(i+1,ts[i][0],ts[i][1])

