import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

class Node(object):
    def __init__(self, num: int):
        self.num = num
        self.cnt = 0
        self.visited = False

def dfs(init_node: Node, graph: list):
    stack = [init_node]
    init_node.visited = True
    while stack:
        cur = stack.pop()
        for nex in graph[cur.num]:
            if nex.visited:
                cur.cnt += nex.cnt
                cur.visited = True
            else:
                stack.append(nex)

n, q = li()
nodes = [Node(i) for i in range(n)]
graph = [[] for _ in range(n)]

for _ in range(n-1):
    ai, bi = li_()
    graph[ai].append(nodes[bi])
    graph[bi].append(nodes[ai])

for _ in range(q):
    pi, xi = li()
    pi -= 1
    nodes[pi].cnt += xi

dfs(nodes[0], graph)

ans = [nodes[i].cnt for i in range(n)]
print(*ans)