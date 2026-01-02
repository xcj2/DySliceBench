
class Node:
    def __init__(self):
        self.parent = -1
        self.type = ""
        self.depth = 0
        self.children = []


def dfs(id, d):
    Nodes[id].depth = d
    for child in Nodes[id].children:
        dfs(child, d+1)


def main():
    n = int(input())
    global Nodes
    Nodes = [Node() for i in range(n)]

    for i in range(n):
        id, k, *c = map(int, input().split())
        Nodes[id].children = c
        if k == 0:
            Nodes[id].type = "leaf"
        else:
            Nodes[id].type = "internal node"
            for j in range(k):
                Nodes[c[j]].parent = id

    rootid = ""
    for i, node in enumerate(Nodes):
        if node.parent == -1:
            rootid = i
    Nodes[rootid].type = "root"
    dfs(rootid, 0)

    for i, node in enumerate(Nodes):
        print("node {}: parent = {}, depth = {}, {}, {}".format(
            i, node.parent, node.depth, node.type, node.children))


if __name__ == '__main__':
    main()
