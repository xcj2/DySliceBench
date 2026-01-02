class Tree:
    def __init__(self, *args):
        self.value, self.left, self.right = args

    def postorder(self):
        left = [] if self.left is None else self.left.postorder()
        right = [] if self.right is None else self.right.postorder()
        return left + right + [self.value]


def recover(pre, ino):
    preord = dict(map(lambda t: (t[1], t[0]), enumerate(pre)))

    def make_tree(tree):
        if len(tree) == 0:
            return None
        root_idx, root_value = min(enumerate(tree), key=lambda t: preord[t[1]])
        return Tree(
            root_value,
            make_tree(tree[:root_idx]),
            make_tree(tree[root_idx + 1:])
        )

    return make_tree(ino).postorder()


if __name__ == '__main__':
    _ = input()
    pre = list(map(int, input().split()))
    ino = list(map(int, input().split()))
    print(' '.join([str(t) for t in recover(pre, ino)]))
