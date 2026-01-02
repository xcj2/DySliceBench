class Tree():
    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)

    def insert(self, z_key):
        self.add_node(z_key)
        z = self.nodes[z_key]
        y = None  # xの親
        x = self.root
        while x is not None:
            y = x  # 親を設定
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def __str__(self):
        ans_in, ans_pre = [], []
        self.root.in_walk(ans_in)
        self.root.pre_walk(ans_pre)
        str_in = ' ' + ' '.join(map(str, ans_in))
        str_pre = ' ' + ' '.join(map(str, ans_pre))
        return str_in + '\n' + str_pre


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def pre_walk(self, ans):
        ans.append(self.key)
        if self.left:
            self.left.pre_walk(ans)
        if self.right:
            self.right.pre_walk(ans)

    def in_walk(self, ans):
        if self.left:
            self.left.in_walk(ans)
        ans.append(self.key)
        if self.right:
            self.right.in_walk(ans)


# ここからmain
tree = Tree()
n = int(input())
for i in range(n):
    line = list(map(str, input().split()))
    if line[0] == 'insert':
        key = int(line[1])
        tree.insert(key)
    else:
        print(tree)

