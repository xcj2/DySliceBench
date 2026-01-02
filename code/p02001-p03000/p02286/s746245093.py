from typing import Optional, List


class Node():
    def __init__(self, key: int, priority: int) -> None:
        self.key = key
        self.priority = priority
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def prewalk(self) -> List[int]:
        ret = [self.key]
        if self.left:
            ret += self.left.prewalk()
        if self.right:
            ret += self.right.prewalk()
        return ret

    def inwalk(self) -> List[int]:
        ret: List[int] = []
        if self.left:
            ret += self.left.inwalk()
        ret += [self.key]
        if self.right:
            ret += self.right.inwalk()
        return ret


class Tree():
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, node: Optional[Node], key: int, priority: int) -> Node:
        if self.root is None:
            self.root = Node(key, priority)
            return self.root
        if node is None:
            return Node(key, priority)
        if key == node.key:
            # Duplicated key case (No insertion).
            return node

        if key < node.key:
            node.left = self.insert(node.left, key, priority)
            if node.priority < node.left.priority:
                node = self._right_rotate(node)
        else:
            node.right = self.insert(node.right, key, priority)
            if node.priority < node.right.priority:
                node = self._left_rotate(node)

        return node

    def _right_rotate(self, t: Node) -> Node:
        assert t.left is not None
        s: Node = t.left
        t.left = s.right
        s.right = t
        return s  # The new root of the subtree.

    def _left_rotate(self, t: Node) -> Node:
        assert t.right is not None
        s: Node = t.right
        t.right = s.left
        s.left = t
        return s  # The new root of the subtree.

    def find(self, key: int) -> Optional[Node]:
        x = self.root
        while x and x.key != key:
            if x.key < key:
                x = x.right
            else:
                x = x.left
        return x

    def delete(self, node: Optional[Node], key: int) -> Optional[Node]:
        if node is None:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            return self._delete(node, key)
        return node

    def _delete(self, node: Node, key: int) -> Optional[Node]:
        if (node.left is None) and (node.right is None):
            return None
        elif node.left is None:
            node = self._left_rotate(node)
        elif node.right is None:
            node = self._right_rotate(node)
        else:
            assert node.left is not None  # Though this is not needed in principle...
            if node.left.priority > node.right.priority:
                node = self._right_rotate(node)
            else:
                node = self._left_rotate(node)
        return self.delete(node, key)

    def _successor(self, x: Node) -> Node:
        assert x is not None
        if x.right:
            return self._minimum(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        assert y is not None
        return y

    def _minimum(self, x: Node) -> Node:
        while x.left:
            x = x.left
        return x

    def print(self) -> None:
        assert self.root is not None
        print('', ' '.join(map(str, self.root.inwalk())))
        print('', ' '.join(map(str, self.root.prewalk())))


if __name__ == "__main__":
    tree = Tree()
    node_num = int(input())
    for _ in range(node_num):
        command, *value = input().split()
        if "insert" == command:
            tree.root = tree.insert(tree.root, int(value[0]), int(value[1]))
        elif "find" == command:
            print('yes' if tree.find(int(value[0])) else 'no')
        elif "delete" == command:
            tree.root = tree.delete(tree.root, int(value[0]))
        elif "print" == command:
            tree.print()
        else:
            pass

