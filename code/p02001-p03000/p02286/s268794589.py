import sys
from collections import namedtuple


Node = namedtuple('Node', ['key', 'priority', 'left', 'right'])


class Treap:
    MAX_KEY = 2000000000
    MAX_PRIORITY = 2000000000

    def __init__(self):
        self.root = None

    def insert(self, key, priority):
        def _insert(node):
            if node is None:
                return Node(key, priority, None, None)
            k, p, left, right = node
            if key < k:
                node = Node(k, p, _insert(left), right)
                if p < node.left.priority:
                    node = self._rotate_right(node)
            elif key > k:
                node = Node(k, p, left, _insert(right))
                if p < node.right.priority:
                    node = self._rotate_left(node)
            else:  # node.key == key
                pass
            # assert(self._bst_invariant(node))
            # assert(self._heap_invariant(node))
            return node

        self.root = _insert(self.root)

    def delete(self, key):
        def _delete(node):
            if node is None:
                return None
            k, p, left, right = node
            if key < k:
                node = node._replace(left=_delete(left))
            elif key > k:
                node = node._replace(right=_delete(right))
            else:  # key == k
                if left is None:
                    node = right
                elif right is None:
                    node = left
                else:
                    if left.priority > right.priority:
                        node = _delete(self._rotate_right(node))
                    else:
                        node = _delete(self._rotate_left(node))
            # assert(self._bst_invariant(node))
            # assert(self._heap_invariant(node))
            return node

        self.root = _delete(self.root)

    def find(self, key):
        def _find(node):
            if node is None:
                return False
            if key < node.key:
                return _find(node.left)
            elif key > node.key:
                return _find(node.right)
            else:
                return True

        return _find(self.root)

    def inorder(self):
        def _inorder(node):
            if node is not None:
                yield from _inorder(node.left)
                yield node
                yield from _inorder(node.right)
        return _inorder(self.root)

    def preorder(self):
        def _preorder(node):
            if node is not None:
                yield node
                yield from _preorder(node.left)
                yield from _preorder(node.right)
        return _preorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node is not None:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node
        return _postorder(self.root)

    def _rotate_left(self, node):
        # assert node.right is not None
        top = node.right
        node = node._replace(right=top.left)
        top = top._replace(left=node)
        return top

    def _rotate_right(self, node):
        # assert node.left is not None
        top = node.left
        node = node._replace(left=top.right)
        top = top._replace(right=node)
        return top

    def _heap_invariant(self, node):
        if node is None:
            return True
        key, priority, left, right = node
        return ((left is None or priority > left.priority)
                and (right is None or priority > right.priority))

    def _bst_invariant(self, node):
        if node is None:
            return True
        key, priority, left, right = node
        return ((left is None or key > left.key)
                and (right is None or key < right.key))

    def __str__(self):
        def _str(node):
            if node is None:
                return ''
            else:
                k, p, l, r = node
                return '({}[{}/{}]{})'.format(_str(l), k, p, _str(r))
        return _str(self.root)


def run():
    input()
    tree = Treap()

    for line in sys.stdin:
        if line.startswith('insert'):
            key, priority = [int(i) for i in line[7:].split()]
            tree.insert(key, priority)
        elif line.startswith('find'):
            if tree.find(int(line[5:])):
                print("yes")
            else:
                print("no")
        elif line.startswith('delete'):
            tree.delete(int(line[7:]))
        elif line.startswith('print'):
            print('', ' '.join([str(n.key) for n in tree.inorder()]))
            print('', ' '.join([str(n.key) for n in tree.preorder()]))
        else:
            raise ValueError('invalid command')
        # print(tree)


if __name__ == '__main__':
    run()

