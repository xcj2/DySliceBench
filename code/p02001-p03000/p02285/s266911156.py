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

    def find(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x
        return None

    def delete(self, key):
        node = self.find(key)
        if node:
            if bool(node.left) ^ bool(node.right):
                node.delete_1()
            elif bool(node.left) & bool(node.right):
                #  2つもつ場合
                next = node.getSuccesor()
                self.delete(next.key)
                node.key = next.key
            else:
                # 1つも持たない場合
                if node.key < node.parent.key:
                    node.parent.left = None
                else:
                    node.parent.right = None

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

    def getSuccesor(self):
        if self.right is not None:
            return self.right.getMinimum()
        p = self.parent
        while (p is not None) & (self == p.right):
            self = p
            p = p.parent
        return p

    def getMinimum(self):
        while self.left is not None:
            self = self.left
        return self

    def delete_1(self):
        p = self.parent
        for c in (self.left, self.right):
            if c:
                c.parent = p
                if self.key < p.key:
                    p.left = c
                else:
                    p.right = c


# ここからmain
tree = Tree()
n = int(input())
for i in range(n):
    line = list(map(str, input().split()))
    if line[0] == 'insert':
        key = int(line[1])
        tree.insert(key)
    elif line[0] == 'find':
        key = int(line[1])
        x = tree.find(key)
        if x:
            print('yes')
        else:
            print('no')
    elif line[0] == 'delete':
        key = int(line[1])
        tree.delete(key)
    else:
        print(tree)

