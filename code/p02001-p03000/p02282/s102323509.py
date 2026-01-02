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
        nodes = {}
        def find(n, li):
            for e1, e2, e3 in li:
                if e1 == n:
                    return (e2, e3)
            raise ValueError()

        def _create(nid):
            if nid in nodes:
                return nodes[nid]
            if nid == -1:
                return None

            lid, rid = find(nid, ids)
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
            for nid in [n[0] for n in nodeids]:
                if all([lid != nid and rid != nid for _, lid, rid in nodeids]):
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

def reconstruct(preorder, inorder):
    """Reconstruct a binary tree from preorder list
    and inorder list of the tree.

    >>> tree = reconstruct([1, 2, 3, 4, 5], [3, 2, 4, 1, 5])
    >>> print(" ".join([str(node) for node in tree.postorder()]))
    3 4 2 5 1
    """
    def _first(li):
        if len(li) > 0:
            return li[0]
        else:
            return -1

    def _reconstruct(_pre, _in):
        assert(len(_pre) == len(_in))
        if len(_pre) == 0:
            return []
        if len(_pre) == 1:
            return [[_pre[0], -1, -1]]
        root, *pre = _pre
        i = _in.index(root)
        in1, in2 = _in[:i], _in[i+1:]
        pre1, pre2 = _pre[1:i+1], _pre[i+1:]
        return ([[root, _first(pre1), _first(pre2)]] +
                _reconstruct(pre1, in1) +
                _reconstruct(pre2, in2))

    return BinaryTree.create(_reconstruct(preorder, inorder))


def run():
    _ = int(input())
    preorder = [int(i) for i in input().split()]
    inorder = [int(i) for i in input().split()]

    tree = reconstruct(preorder, inorder)
    print(" ".join([str(n) for n in tree.postorder()]))


if __name__ == '__main__':
    run()

