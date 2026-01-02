from sys import stdin, stdout
from collections import defaultdict
def readcase(o):
    line = o.readline()
    if not line: return None, None
    line = line.strip().split()
    # print(len(line))
    # print(line[0], line[1])

    return int(line[0]), int(line[1])

def tarjan(g):
    sources = list(g.keys())
    # visited = set()
    artPoints = set()
    time = {}
    low = {}
    parent = {}
    # ancestors = defaultdict(set)
    children = defaultdict(set)
    visitedTime = defaultdict(int)
    ti=0


    def dfs(u, stack):
        nonlocal ti
        while stack:
            u = stack[-1]
            visitedTime[u]+=1
            # Initialize discovery time and low value 
            if u not in time:
                time[u] = ti
                low[u] = ti
                ti += 1 
            currChildren = 0
            for v in g[u]: 
                if v not in time: 
                    parent[v]=u
                    children[u].add(v)
                    currChildren+=1
                    stack.append(v)
                    break
                if v in children[u]:
                    low[u] = min(low[u], low[v]) 
                    if u in parent and low[v] >= time[u]:
                        artPoints.add(u)
                        # print(time[u], low[u], time[v], low[v])
                    if u not in parent and len(children[u])>1:
                        artPoints.add(u)
                        # print(time[u], low[u], time[v], low[v])
                elif u not in parent or parent[u] != v:
                    low[u] = min(low[u], time[v]) 
            if currChildren == 0:
                stack.pop()
    for s in sources:
        if s not in time:
            stack = [s]
            dfs(s, stack)
            ti=0
    ans = sorted(list(artPoints))
    for i, a in enumerate(ans):
        print(a)

if __name__ == '__main__':
    g = defaultdict(list)
    solutions = None
    u, v = readcase(stdin)
    if not (not u or u == 0):
        while 1:   
            u, v = readcase(stdin)
            if u == None:
                break
            if u != v:
                g[u].append(v)
                g[v].append(u)


        tarjan(g)
        # solutions = [str(y) for y in solutions]
        # solutions = "\n".join(solutions)
        # print(solutions, end="")
    # print("2")
    # print(solutions)

