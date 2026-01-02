class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        p = None # parent
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while n is not None:
                p = n
                if data < n.data:
                    n = n.left
                else:
                    n = n.right

            if (data < p.data):
              p.left = Node(data)
            else:
              p.right = Node(data)

    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,node):
        if node is not None:
            self._inorder(node.left)
            print(" " + str(node.data), end="")
            self._inorder(node.right)
    def preorder(self):
        self._preorder(self.root)
    def _preorder(self,node):
        if node is not None:
            print(" " + str(node.data), end="")
            self._preorder(node.left)
            self._preorder(node.right)

n = int(input())
t = BST()
for i in range(0, n):
  line = input().split()

  if line[0] == "insert":
    t.insert(int(line[1]))
  elif line[0] == "print":
    t.inorder()
    print()
    t.preorder()
    print()
