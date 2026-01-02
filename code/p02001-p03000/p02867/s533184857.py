class UnionFindNode(object):
    """
    Union-Find構造
    ノードのグループ併合や、所属グループ判定を高速に処理する
    """

    def __init__(self, group_id, parent=None, value=None):
        self.group_id_ = group_id
        self.parent_ = parent
        self.value = value
        self.size_ = 1

    def __str__(self):
        template = "UnionFindNode(group_id: {}, \n\tparent: {}, value: {}, size: {})"
        return template.format(self.group_id_, self.parent_, self.value, self.size_)

    def is_root(self):
        return not self.parent_

    def root(self):
        parent = self
        while not parent.is_root():
            parent = parent.parent_
            self.parent_ = parent
        return parent

    def find(self):
        parent = self.root()
        return parent.group_id_

    def size(self):
        parent = self.root()
        return parent.size_

    def unite(self, unite_node):
        parent = self.root()
        unite_parent = unite_node.root()

        if parent.group_id_ != unite_parent.group_id_:
            if parent.size() > unite_parent.size():
                unite_parent.parent_ = parent
                parent.size_ = parent.size_ + unite_parent.size_
            else:
                parent.parent_ = unite_parent
                unite_parent.size_ = parent.size_ + unite_parent.size_

    def same(self, node):
        return self.root() == node.root()


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = list(zip(a, b))
l.sort(key=lambda x: x[1])
a.sort()
d = dict()
for i, x in enumerate(a):
    d[x] = i
b.sort()
for i in range(n):
    if a[i] > b[i]:
        print('No')
        exit(0)
for i in range(n - 1):
    if a[i + 1] <= b[i]:
        print('Yes')
        exit(0)
uf = [UnionFindNode(i) for i in range(n)]
al = [d[x[0]] for x in l]
for i in range(n):
    uf[i].unite(uf[al[i]])
if uf[0].root().size() == n:
    print('No')
else:
    print('Yes')
