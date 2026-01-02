import sys

N=int(input())
sys.setrecursionlimit(100000)
u = [0]*(N-1)
v = [0]*(N-1)
w = [0]*(N-1)
for i in range(N-1):
    u[i], v[i], w[i] = map(int, input().split())
    u[i] -= 1
    v[i] -= 1

class Path:
    def __init__(self, next_node, length, num):
        self.next=next_node
        self.len=length
        self.num=num

class Node:
    def __init__(self, index):
        self.index = index
        self.paths = []

    def append(self, next_node, length, num):
        self.paths.append(Path(next_node, length, num))

nodes = [Node(i) for i in range(N)]
for i in range(N-1):
    nodes[u[i]].append(v[i], w[i], i)
    nodes[v[i]].append(u[i], w[i], i)

past_paths = [0]*(N-1)
paints = [-1]*N

def rec(pos, color):
    if paints[pos] == -1:
        paints[pos] = color
    for path in nodes[pos].paths:
        # まだ通ってない道を通る
        if past_paths[path.num] == 0:
            past_paths[path.num] = 1
            rec(path.next, (color + path.len) % 2)
        # さっきの道を戻ってくる

rec(0, 0)

for i in paints:
    print(i)
