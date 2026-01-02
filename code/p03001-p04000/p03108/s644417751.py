class DisjointSet(object):
    class Node(object):
        def __init__(self, number: int):
            self.number = number  # int
            self.parent = None    # Node  根　　ではNone
            self.rank = 0         # int   根以外ではNone

            self.linked_num = 1

        def is_root(self):
            return self.parent is None

        def find_root(self) -> "Node":
            if self.is_root():
                return self

            # 木をなるべく低くするために，根に直結させる
            self.parent = self.parent.find_root()
            self.rank = None
            return self.parent

    def __init__(self, size: int):
        self.size = size
        self.nodes = list(map(lambda i: self.Node(i), range(size)))

    def get_node(self, number: int) -> Node:
        if number < 0 or self.size <= number:
            raise ValueError("number out of range")

        return self.nodes[number]

    def unite(self, left_node: Node, right_node: Node) -> "DisjointSet":
        if left_node.number < 0 or self.size <= left_node.number:
            raise ValueError("not existing left_node")

        if right_node.number < 0 or self.size <= right_node.number:
            raise ValueError("not existing right_node")

        left_root = left_node.find_root()
        right_root = right_node.find_root()
        if left_root is right_root:
            return self

        # rank の大きい木をベースに結合
        if left_root.rank < right_root.rank:
            left_root.parent = right_root
            left_root.rank = None

        elif left_root.rank > right_root.rank:
            right_root.parent = left_root
            right_root.rank = None

        else:  # left_root.rank == right_root.rank
            # どちらに結合してもよく，このときだけ rank を1増やす
            right_root.parent = left_root
            right_root.rank = None
            left_root.rank += 1

        root = left_root.find_root()
        root.linked_num = left_root.linked_num + right_root.linked_num
        return self

    def have_same_root(self, left_node: Node, right_node: Node) -> bool:
        if left_node.number < 0 or self.size <= left_node.number:
            raise ValueError("not existing left_node")

        if right_node.number < 0 or self.size <= right_node.number:
            raise ValueError("not existing right_node")

        return left_node.find_root() is right_node.find_root()


if __name__ == '__main__':
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    comb = N * (N-1) // 2

    ans = [comb]
    linked_num = [1 for _ in range(N+1)]
    disjointSet = DisjointSet(N+1)

    for a, b in zip(reversed(A), reversed(B)):
        node_a, node_b = disjointSet.get_node(a), disjointSet.get_node(b)
        if disjointSet.have_same_root(node_a, node_b):
            ans.append(ans[-1])
        else:
            linked_num_a = node_a.find_root().linked_num
            linked_num_b = node_b.find_root().linked_num
            ans.append(ans[-1] - linked_num_a * linked_num_b)
            disjointSet.unite(node_a, node_b)

    print('\n'.join(map(str, reversed(ans[:-1:]))))
