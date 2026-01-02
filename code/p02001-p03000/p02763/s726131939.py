def main():
    import sys
    buf = sys.stdin.buffer

    class SegmentTree:
        def __init__(self, target, no_effect):
            target_size = len(target)
            leaves_size = 1
            while leaves_size < target_size:
                leaves_size *= 2
            self.tree_size = leaves_size * 2 - 1
            self.tree = [no_effect] * self.tree_size
            self.no_effect = no_effect
            self.initialize_tree(target)

        @classmethod
        def initialize_func(cls, value):
            return 1 << (ord(value) - ord('a'))

        @classmethod
        def merge_func(cls, a, b):
            return a | b

        def merge_child_data(self, node):
            child1 = node * 2 + 1
            child2 = node * 2 + 2
            merged = self.merge_func(self.tree[child1], self.tree[child2])
            return merged

        def initialize_tree(self, target):
            initial_leaf = self.tree_size // 2
            leaves = range(initial_leaf, initial_leaf+len(target))
            for value, leaf in zip(target, leaves):
                self.tree[leaf] = self.initialize_func(value)

            for parent in range(initial_leaf-1, -1, -1):
                self.tree[parent] = self.merge_child_data(parent)

        def update(self, new_value, index):
            leaf = self.tree_size//2 + index
            new_data = self.initialize_func(new_value)
            if self.tree[leaf] == new_data:
                return
            self.tree[leaf] = new_data

            parent = (leaf-1) // 2
            while parent >= 0:
                new_data = self.merge_child_data(parent)
                if self.tree[parent] == new_data:
                    break
                self.tree[parent] = new_data
                parent = (parent-1) // 2

        def resolve_query(self, _from, to):
            result = self.no_effect
            left, right = _from + self.tree_size//2, to + self.tree_size//2
            while left <= right:
                result = self.merge_func(result, self.tree[left])
                result = self.merge_func(result, self.tree[right])
                left //= 2
                right = right//2 - 1

            return bin(result).count('1')

    n, S, _, *queries = buf.read().split()
    S = S.decode()
    seg_tree = SegmentTree(target=S, no_effect=0)

    for type, a, b in zip(*[iter(queries)]*3):
        if type == b'1':
            index, new = int(a)-1, b
            seg_tree.update(new, index)

        elif type == b'2':
            _from, to = int(a)-1, int(b)-1
            print(seg_tree.resolve_query(_from, to))


if __name__ == '__main__':
    main()
