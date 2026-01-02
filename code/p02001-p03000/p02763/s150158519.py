from functools import reduce
import sys
input = sys.stdin.readline


class SegmentTrees:
    def __init__(self, target, no_effect):
        size = len(target)
        length = 1
        while length < size:
            length *= 2
        self.tree_size = length * 2 - 1
        self.tree = [no_effect] * self.tree_size
        self.areas = [[0, 0] for _ in range(self.tree_size)]
        self.set_areas()
        self.initialize_tree_by_target(target, no_effect)
        self.target = target

    def set_areas(self):
        def decide_children_areas(node):
            left, right = self.areas[node]
            center = (left+right)//2
            child1 = node * 2 + 1
            child2 = node * 2 + 2
            self.areas[child1] = [left, center]
            self.areas[child2] = [center+1, right]

        self.areas[0] = [0, self.tree_size//2]
        for parent in range(self.tree_size//2):
            decide_children_areas(parent)

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

    def initialize_tree_by_target(self, target: list, no_effect=0):
        def calc_leafs():
            initial_leaf = self.tree_size//2
            leafs = range(initial_leaf, initial_leaf+len(target))
            for value, leaf in zip(target, leafs):
                self.tree[leaf] = self.initialize_func(value)

            residue = range(initial_leaf+len(target), self.tree_size)
            for residual_leaf in residue:
                self.tree[residual_leaf] = no_effect

        calc_leafs()
        for parent in range(self.tree_size//2-1, -1, -1):
            self.tree[parent] = self.merge_child_data(parent)

    def update(self, new_data, position):
        leaf = self.tree_size//2 + position
        new = self.initialize_func(new_data)
        if self.tree[leaf] == new:
            return
        self.tree[leaf] = new
        parent = (leaf-1) // 2
        while parent >= 0:
            new = self.merge_child_data(parent)
            if self.tree[parent] == new:
                break
            self.tree[parent] = new
            parent = (parent-1) // 2

    def get_query(self, _from, to):
        def get_tree_data(node):
            left, right = self.areas[node]
            if _from <= left and right <= to:
                result.append(self.tree[node])
                return
            if to < left or right < _from:
                return

            child1 = node * 2 + 1
            child2 = node * 2 + 2
            get_tree_data(child1)
            get_tree_data(child2)

        result = []
        get_tree_data(0)
        ans = reduce(self.merge_func, result)
        ans = bin(ans).count('1')
        return ans


n = int(input())
S = input().replace('\n', '')
seg_tree = SegmentTrees(target=S, no_effect=0)

Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        position, new = int(query[1])-1, query[2]
        seg_tree.update(new, position)

    elif query[0] == '2':
        _from, to = int(query[1])-1, int(query[2])-1
        print(seg_tree.get_query(_from, to))