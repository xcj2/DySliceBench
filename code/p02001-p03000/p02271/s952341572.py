class Tree:
    class Node:
        def __init__(self, n, left, right):
            self.left = left
            self.right = right
            self.n = n
            if left is not None:
                lt = {t + n for t in left.totals}
            else:
                lt = set()
            if right is not None:
                rt = right.totals
            else:
                rt = set()

            self.totals = lt | rt | {n}

        def find(self, total):
            return total in self.totals

        def __str__(self):
            cs = []
            if self.left is not None:
                cs.append(str(self.left))
            if self.right is not None:
                cs.append(str(self.right))

            return "{} -> ({})".format(self.n, ",".join(cs))


    def __init__(self, ns):
        self.top = self.build_nodes(sorted(ns))

    def has_subset(self, total):
        return self.top.find(total)

    def build_nodes(self, ns):
        if len(ns) == 0:
            return None

        left = self.build_nodes(ns[:-1])
        right = self.build_nodes(ns[:-1])
        node = self.Node(ns[-1], left, right)

        return node


def run_tree():
    _ = int(input())  # flake8: noqa
    ns = [int(i) for i in input().split()]

    tree = Tree(ns)
    _ = int(input())  # flake8: noqa

    for q in (int(j) for j in input().split()):
        if tree.has_subset(q):
            print("yes")
        else:
            print("no")



if __name__ == '__main__':
    run_tree()

