import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    n = int(input().strip())
    tree = defaultdict(list)
    parent = [-1] * n

    for i in range(n):
        line = [int(j) for j in input().strip().split()]
        tree[line[0]] += line[2:]
        for j in line[2:]:
            parent[j] = line[0] 

    depth = [9999] * n
    _root = parent.index(-1)
    depth[_root] = 0

    def fill_depth(tree, n, d):
        depth[n] = d
        links = tree[n]
        for l in links:
            fill_depth(tree, l, d + 1)
    
    fill_depth(tree,_root,0)
    
    def get_attr(tree, n, root):
        if n == root:
            return "root"
        elif len(tree[n]) > 0:
            return "internal node"
        else:
            return "leaf"
    
    for i in range(n):
        print("node {}: parent = {}, depth = {}, {},".format(i,parent[i],depth[i],get_attr(tree,i,_root)),tree[i])

if __name__ == "__main__":
    main()
