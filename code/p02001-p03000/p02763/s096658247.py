import sys
input = sys.stdin.readline


class SegmentTrees:
    def __init__(self, target, no_effect):
        target_size = len(target)
        leaves_size = 1
        while leaves_size < target_size:
            leaves_size *= 2
        self.tree_size = leaves_size * 2 - 1
        self.tree = [no_effect] * self.tree_size
        self.no_effect = no_effect
        self.initialize_tree(target, no_effect)

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

    def initialize_tree(self, target: list, no_effect=0):
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
        def is_in_query(left, right):
            if _from <= left and right <= to:
                return 1
            elif to < left or right < _from:
                return 0
            else:
                return -1

        node = 0
        left, right = 0, self.tree_size//2
        todo = [[node, left, right]]

        result = self.no_effect
        while todo:
            node, left, right = todo.pop()
            if is_in_query(left, right) == 1:
                data = self.tree[node]
                result = self.merge_func(result, data)

            elif is_in_query(left, right) == 0:
                continue

            else:
                child1 = node * 2 + 1
                child2 = node * 2 + 2
                center = (left+right)//2
                todo.append([child1, left, center])
                todo.append([child2, center+1, right])

        return bin(result).count('1')


n = int(input())
S = input().replace('\n', '')
seg_tree = SegmentTrees(target=S, no_effect=0)

Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        index, new = int(query[1])-1, query[2]
        seg_tree.update(new, index)

    elif query[0] == '2':
        _from, to = int(query[1])-1, int(query[2])-1
        print(seg_tree.resolve_query(_from, to))
