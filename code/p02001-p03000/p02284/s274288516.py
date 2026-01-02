class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, insert_node):
        p = None
        r = self.root
        while r:
            p = r
            if insert_node.value < r.value:
                r = r.left
            else:
                r = r.right

        if not p:
            self.root = insert_node
        elif insert_node.value < p.value:
            p.left = insert_node
        else:
            p.right = insert_node

    def find(self, find_value):
        p = None
        r = self.root
        while r:
            p = r
            if find_value == r.value:
                return "yes"
            if find_value < r.value:
                r = r.left
            else:
                r = r.right
        return "no"

class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left  = left
        self.right = right

    def pre_order_search(self):
        l = self.left
        r = self.right
        print("",self.value, end="")
        if l:
            l.pre_order_search()
        if r:
            r.pre_order_search()

    def in_order_search(self):
        l = self.left
        r = self.right
        if l:
            l.in_order_search()
        print("",self.value, end="")
        if r:
            r.in_order_search()

m = int(input())
tree = BinaryTree()

for i in range(m):
    inp = input().split()
    if inp[0] == "insert":
        tree.insert(Node(int(inp[1]), None, None))
    elif inp[0] == "find":
        print(tree.find(int(inp[1])))
    else:
        tree.root.in_order_search()
        print()
        tree.root.pre_order_search()
        print()