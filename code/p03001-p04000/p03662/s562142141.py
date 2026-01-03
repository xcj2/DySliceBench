#!python3

import sys
sys.setrecursionlimit(10 ** 6)


class Node:

    def __init__(self, num):
        self.num = num
        self.v = 1
        self.parent = 0
        self.deep = None


def LI():
    return list(map(int, input().split()))

# input
N = int(input())
AB = [LI() for _ in range(N - 1)]

# link
link = [[] for _ in range(N + 1)]
for a, b in AB:
    link[a].append(b)
    link[b].append(a)

# nodes
nodes = [Node(i) for i in range(N + 1)]


def create_tree(parent):
    for child in link[parent.num]:
        if child == parent.parent:
            continue
        node = nodes[child]
        node.parent = parent.num
        node.deep = parent.deep + 1
        create_tree(node)
        parent.v += node.v


def main():
    nodes[1].deep = 1
    create_tree(nodes[1])

    x = (nodes[N].deep - nodes[1].deep - 1) // 2
    v = nodes[N]
    for _ in range(x):
        v = nodes[v.parent]
    
    snuke = v.v
    fennec = N - snuke
    ans = "Fennec" if fennec > snuke else "Snuke"
    print(ans)


if __name__ == "__main__":
    main()
