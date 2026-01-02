class Tree:
    def __init__(self, N):
        self.N = N
        self.nodes = [ Node(i) for i in range(N) ]

    def get_root(self, node):
        if node.parent is None:
            return node
        root = self.get_root(node.parent)
        node.parent = root
        return root

    def merge(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)

        if root1.ID == root2.ID:
            return

        root1.parent = root2

    def get_root_count(self):
        count = 0
        for n in self.nodes:
            if n.parent is None:
                count += 1
        return count

class Node:
    def __init__(self, ID):
        self.ID = ID
        self.parent = None

def main():
    N, M = map(int, input().split())
    tree = Tree(N)
    for i in range(M):
        A, B = map(int, input().split())
        A, B = A-1, B-1
        tree.merge(tree.nodes[A], tree.nodes[B])
    print(tree.get_root_count() - 1)


main()
