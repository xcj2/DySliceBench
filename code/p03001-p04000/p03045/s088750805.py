class UnionFindTree:
    _node_num = 0
    _parent_list = []
    _tree_len = []
    _num_trees = 0

    def __init__(self, node_num):
        self._node_num = node_num
        self._parent_list = [-1 for i in range(node_num+1)]
        self._tree_len = [0 for i in range(node_num+1)]
        self._num_trees = node_num

    def _root(self, node):
        root = node
        while self._parent_list[root] != -1:
            root = self._parent_list[root]
        return root

    def union(self, x, y):
        xr = self._root(x)
        yr = self._root(y)
        if xr == yr:
            return
        if self._tree_len[xr] < self._tree_len[yr]:
            self._parent_list[xr] = yr
            self._tree_len[yr] += 1
        else:
            self._parent_list[yr] = xr
            self._tree_len[xr] += 1
        self._num_trees -= 1

    def get_num_trees(self):
        return self._num_trees

def main():
    N, M = map(int, input().split())

    uft = UnionFindTree(N)
    for i in range(M):
        x, y, z = map(int, input().split())
        uft.union(x, y)
    print(uft.get_num_trees())

if __name__ == '__main__':
    main()
