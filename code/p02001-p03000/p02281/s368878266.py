class BinaryTree:
    class Node:
        def __init__(self, nid, left, right):
            self.id = nid
            self.left = left
            self.right = right

        def has_left(self):
            return self.left is not None

        def has_right(self):
            return self.right is not None

        def __str__(self):
            return str(self.id)

    @classmethod
    def create(cls, ids):
        nodes = [None] * len(ids)

        def _create(nid):
            if nid in nodes:
                return nodes[nid]
            if nid == -1:
                return None

            lid, rid = ids[nid]
            if lid == -1 and rid == -1:
                right = None
                left = None
            elif lid == -1:
                right = _create(rid)
                left = None
            elif lid == -1:
                right = None
                left = _create(lid)
            else:
                right = _create(rid)
                left = _create(lid)
            nodes[nid] = cls.Node(nid, left, right)
            return nodes[nid]

        def _root(nodeids):
            for nid in range(len(nodeids)):
                if all([lid != nid and rid != nid for lid, rid in nodeids]):
                    return nid

        root = _create(_root(ids))
        return cls(root)

    def __init__(self, root):
        self.root = root

    def preorder(self):
        def _preorder(node):
            yield node
            if node.has_left():
                yield from _preorder(node.left)
            if node.has_right():
                yield from _preorder(node.right)
        yield from _preorder(self.root)

    def inorder(self):
        def _inorder(node):
            if node.has_left():
                yield from _inorder(node.left)
            yield node
            if node.has_right():
                yield from _inorder(node.right)
        yield from _inorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node.has_left():
                yield from _postorder(node.left)
            if node.has_right():
                yield from _postorder(node.right)
            yield node
        yield from _postorder(self.root)


def run():
    n = int(input())

    nodeids = [None] * n
    for i in range(n):
        nid, lid, rid = [int(x) for x in input().split()]
        nodeids[nid] = [lid, rid]

    tree = BinaryTree.create(nodeids)

    print('Preorder')
    for node in tree.preorder():
        print(" {}".format(node), end="")
    print()
    print('Inorder')
    for node in tree.inorder():
        print(" {}".format(node), end="")
    print()
    print('Postorder')
    for node in tree.postorder():
        print(" {}".format(node), end="")
    print()


if __name__ == '__main__':
    run()

