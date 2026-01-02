class Node:

    def __init__(self, _id):
        self.id = _id
        self.left = None
        self.right = None
        self.parent = None

    def add_left(self, node):
        node.parent = self
        self.left = node

    def add_right(self, node):
        node.parent = self
        self.right = node

    @property
    def parent_id(self):
        if self.parent is None:
            return -1
        else:
            return self.parent.id

    @property
    def deg(self):
        count = 0
        if self.right is not None:
            count += 1
        if self.left is not None:
            count += 1
        return count

    @property
    def sibling_id(self):
        if self.parent is None or self.parent.deg == 1:
            return -1
        else:
            if self.parent.left == self:
                return self.parent.right.id if self.parent.right is not None else -1
            else:
                return self.parent.left.id if self.parent.left is not None else -1

    @property
    def node_type(self):
        if self.parent is None:
            return 'root'
        if self.left is None and self.right is None:
            return 'leaf'
        return 'internal node'

    @property
    def height(self):
        if self.left is None:
            left = -1
        else:
            left = self.left.height
        if self.right is None:
            right = -1
        else:
            right = self.right.height
        return max(left, right) + 1

    @property
    def depth(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.depth + 1

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return 'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
            self.id, self.parent_id, self.sibling_id, self.deg, self.depth, self.height, self.node_type)


def main():
    n = int(input())
    nodes = [Node(i) for i in range(n)]
    for _ in range(n):
        ID, left, right = map(int, input().split(' '))
        if left != -1:
            nodes[ID].add_left(nodes[left])
        if right != -1:
            nodes[ID].add_right(nodes[right])
    for node in nodes:
        print(node)


if __name__ == '__main__':
    main()

