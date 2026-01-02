class Tree():
    def __init__(self):
        self.nodes = {}
        self.root = None
        self.nodes[-1] = None

    def add_node(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)

    def add_child(self, parent_id, left_id, right_id):
        self.add_node(parent_id)
        self.add_node(left_id)
        self.add_node(right_id)
        self.nodes[parent_id].add_child(self.nodes[left_id], self.nodes[right_id])

    def set_root(self):
        for id in self.nodes:
            if id == -1:
                continue
            if self.nodes[id].parent is None:
                self.root = self.nodes[id]


class Node():
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.right = None
        self.left = None

    def add_child(self, left, right):
        self.left = left
        self.right = right
        # -1ならNoneが代入される
        for c in [left, right]:
            if c:
                c.parent = self

    def pre_walk(self, ans):
        ans.append(self.id)
        if self.left:
            self.left.pre_walk(ans)
        if self.right:
            self.right.pre_walk(ans)

    def in_walk(self, ans):
        if self.left:
            self.left.in_walk(ans)
        ans.append(self.id)
        if self.right:
            self.right.in_walk(ans)

    def post_walk(self, ans):
        if self is None:
            pass
        else:
            if self.left:
                self.left.post_walk(ans)
            if self.right:
                self.right.post_walk(ans)
            ans.append(self.id)


n = int(input())
tree = Tree()
for i in range(n):
    tmp = list(map(int, input().split()))
    id = tmp[0]
    left, right = tmp[1:]
    tree.add_node(id)
    tree.add_child(id, left, right)

tree.set_root()
for i in range(3):
    ans = []
    if i == 0:
        print('Preorder')
        tree.root.pre_walk(ans)
    if i == 1:
        print('Inorder')
        tree.root.in_walk(ans)
    if i == 2:
        print('Postorder')
        tree.root.post_walk(ans)

    print('', *ans)

