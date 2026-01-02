class tree:
    def __init__(self,n):
        self.edge = [set() for i in range(n)]
    def add_edge_dual(self,f,e):
        self.edge[f].add(e)
        self.edge[e].add(f)
    def add_edge_single(self,f,e):
        self.edge[f].add(e)
    def connected(self,node):
        return self.edge(node)


def dfs(graph,s):
    visited = [False for i in range(len(graph.edge))]
    distance = [-1 for i in range(len(visited))]
    visited[s] = True
    distance[s] = 0
    buf = [[s]]
    now = s
    while len(buf) != 0:
        nexts = buf[0]
        buf = buf[1:]
        temp = []
        for nex in nexts:
            for child in graph.edge[nex]:
                if visited[child] == False:
                    distance[child] = distance[nex]+1
                    temp.append(child)
                    visited[child] = True
                else:
                    continue
        if len(temp) == 0:
            continue
        else:
            buf.append(temp)
    return  distance



n,u,v = map(int,input().split())
t = tree(n)

for i in range(n-1):
    a,b = map(int,input().split())
    t.add_edge_dual(a-1,b-1)

taka = dfs(t,u-1)
aoki = dfs(t,v-1)

aofar = -1
for i in range(n):
    if taka[i] < aoki[i]:
        if aoki[i] > aofar:
            aofar = aoki[i]


print(aofar-1)

# print(sorted(taka,key=lambda x:-x))
# print(sorted(aoki,key=lambda x:-x))
#
# print()
# print(far,aofar)