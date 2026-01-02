from collections import UserList
class Stack(UserList):
    def __init__(self):
        UserList.__init__(self)
        self.contains = set()
    def __contains__(self, x):
        return x in self.contains
    def __and__(self, x):
        return self.contains & x
    def push(self, x):
        if x in self.contains:
            return
        self.data.append(x)
        self.contains |= {x}
    def pop(self):
        x = self.data.pop()
        self.contains -= {x}
        return x

def search(g, g_dash,v):
    # search postorder
    visited = set()
    postorder = []
    for root in range(v):
        if root in visited:
            continue
        route = Stack()
        route.push(None)
        dfs_stack = [(root, None)]            
        while dfs_stack:
            u, prev = dfs_stack.pop()
            if u in visited:
                continue
            visited |= {u}
            dfs_stack.extend((v, u) for v in g[u] - visited)
            while route[-1] != prev:
                postorder.append(route.pop())
            route.push(u)
        while route[-1] is not None:
            postorder.append(route.pop())

    # reverse search lowest
    visited.clear()
    lowest = [None] * v
    for root in postorder[::-1]:
        if root in visited:
            continue
        dfs_stack = [root]
        while dfs_stack:
            u = dfs_stack.pop()
            if u in visited:
                continue
            visited |= {u}
            lowest[u] = root
            dfs_stack.extend(g_dash[u] - visited)
    return lowest

from sys import stdin
from collections import defaultdict
readline = stdin.readline

def main():
    v, e = map(int, readline().split())
    g = defaultdict(set)
    g_dash = defaultdict(set)

    for _ in range(e):
        s, t = map(int, readline().split())
        g[s] |= {t}        
        g_dash[t] |= {s}        
    
    lowest = search(g,g_dash, v)
    q = int(readline())
    for u, v in [map(int, readline().split()) for _ in range(q)]:
        print(1 if lowest[u] == lowest[v] else 0)
main()