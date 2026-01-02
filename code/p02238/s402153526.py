n = int(input())
graph = {}
ans = []
np = set(range(1,n+1))
for i in range(n):
    t = list(map(int, input().split()))
    v = t[0]
    k = t[1]
    graph[v] = [t[i+2] for i in range(k)]
    np=np - set(graph[v])
    ans.append([v,None,None])

class Time:
    def __init__(self):
        self.time = 0
    def getTime(self):
        self.time += 1
        return self.time

t = Time()

visited = set()
def dfs(graph, target):
    visited.add(target)
    # ???????????????????¨????
    if ans[target - 1][1] is None:
        ans[target - 1][1] = t.getTime()
    if graph[target] == []:
        if ans[target - 1][2] is None:
            ans[target - 1][2] = t.getTime()        
        return
    for v in sorted(graph[target]):
        # # ???????????????????¨????
        if v not in visited:        
            if ans[v - 1][1] is None:
                ans[v - 1][1] = t.getTime()        
            visited.add(target)
            dfs(graph,v)
    if ans[target - 1][2] is None:
        ans[target - 1][2] = t.getTime()

if np == set():
    np = [1]
for v in sorted(list(np)):
    dfs(graph,v)
for row in ans:
    print(*row)