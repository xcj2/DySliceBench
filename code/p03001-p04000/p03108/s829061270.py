
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.rank = 0
        self.elements_count = 1


class DisjointSet:
    def __init__(self, nodes):
        self.nodes = nodes

    def find_set(self, key):
        pivot = self.nodes[key]
        while pivot.key != pivot.parent.key:
            pivot = pivot.parent
        self.nodes[key].parent = pivot
        return pivot.key

    def elements_count(self, key):
        repr_key = self.find_set(key)
        return self.nodes[repr_key].elements_count

    def same(self, x, y):
        return self.find_set(x) == self.find_set(y)

    def unite(self, x, y):
        y_root = self.find_set(y)
        x_root = self.find_set(x)
        if self.nodes[x].rank > self.nodes[y].rank:
            self.nodes[y_root].parent = self.nodes[x_root]
            self.nodes[x_root].elements_count += self.nodes[y_root].elements_count
        elif self.nodes[x].rank < self.nodes[y].rank:
            self.nodes[x_root].parent = self.nodes[y_root]
            self.nodes[y_root].elements_count += self.nodes[x_root].elements_count
        else:
            self.nodes[x_root].parent = self.nodes[y_root]
            self.nodes[y_root].rank = self.nodes[y_root].rank + 1
            self.nodes[y_root].elements_count += self.nodes[x_root].elements_count


def comb_pair(n):
    return (n * (n - 1)) // 2


def m():
    N, M = [int(i) for i in input().split()]
    nodes = [Node(i) for i in range(0, N)]
    for node in nodes:
        node.parent = node
    ds = DisjointSet(nodes)

    convenience = [0] * (M + 1)
    inputs = [input().split() for _ in range(M)]
    inputs = [(int(x[0]) - 1, int(x[1]) - 1) for x in inputs]
    reversed_inputs = list(reversed(inputs))
    for i in range(M):
        a, b = reversed_inputs[i]
        if ds.same(a, b):
            convenience[i+1] = convenience[i]
            next
        else:
            before = comb_pair(ds.elements_count(a)) + comb_pair(ds.elements_count(b))
            ds.unite(a, b)
            after = comb_pair(ds.elements_count(a))
            diff = after - before
            convenience[i+1] = convenience[i] + diff
    maximum = convenience[-1]
    for c in convenience[-2::-1]:
        print(maximum - c)


if __name__ == '__main__':
    m()
