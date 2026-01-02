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
        r = self.root
        while r:
            if find_value == r.value:
                return "yes"
            if find_value < r.value:
                r = r.left
            else:
                r = r.right
        return "no"

    def delete(self, delete_value):
        flag = None
        p = None
        r = self.root
        while True:
            if delete_value == r.value:
                if r.left == None and r.right == None:
                    if flag == "l":
                        p.left = None
                    else:
                        p.right = None
                    return
                elif r.left == None:
                    if flag == "l":
                        p.left = r.right
                    else:
                        p.right = r.right
                    return
                elif r.right == None:
                    if flag == "l":
                        p.left = r.left
                    else:
                        p.right = r.left
                    return
                else:
                    min_node = r.right
                    while min_node:
                        p = min_node
                        min_node = min_node.left
                    swap_value = p.value
                    self.delete(swap_value)
                    r.value = swap_value
                    return
            elif delete_value < r.value:
                p = r
                r = r.left
                flag = "l"
            else:
                p = r
                r = r.right
                flag = "r"

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
    elif inp[0] == "delete":
        tree.delete(int(inp[1]))
    else:
        tree.root.in_order_search()
        print()
        tree.root.pre_order_search()
        print()