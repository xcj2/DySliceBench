import sys
input = sys.stdin.readline

def unite(node_a, node_b):
    root_a = node_a.root()
    root_b = node_b.root()
    if root_a == root_b:
        return False
    if root_b.depth > root_a.depth:
        root_a, root_b = root_b, root_a
    root_b.is_root = False
    root_b.parent = root_a
    root_a.depth = max(root_a.depth, root_b.depth+1)
    return True

class Node:
    def __init__(self, id):
        self.id = id
        self.is_root = True
        self.parent = None
        self.depth = 1
    
    def root(self):
        # if self.is_root:
        #     return self
        # elif self.parent.is_root:
        #     return self.parent
        # else:
        #     self.parent = self.parent.root()
        #     return self.parent
        node = self
        while not node.is_root:
            node = node.parent
        return node

def main():
    N, K, L = map(int, input().split())
    
    trains = [Node(i) for i in range(N)]
    streets = [Node(i) for i in range(N)]

    for i in range(K):
        p, q = map(int, input().split())
        p -= 1; q -= 1
        unite(trains[p], trains[q])
    for i in range(L):
        r, s = map(int, input().split())
        r -= 1; s -= 1
        unite(streets[r], streets[s])
    dic = {}
    roots = []
    for i in range(N):
        tmp = (trains[i].root().id, streets[i].root().id)
        roots.append(tmp)
        if tmp in dic:
            dic[tmp] += 1
        else:
            dic[tmp] = 1
    
    for i in range(N-1):
        print(dic[roots[i]], end=" ")
    print(dic[roots[N-1]])

if __name__ == "__main__":
    main()