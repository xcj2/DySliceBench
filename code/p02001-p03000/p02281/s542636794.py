class Node():
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None
        self.parent = None
        self.marked = 0
    def setLeft(self, left):
        left.parent = self
        self.left = left
    def setRight(self, right):
        right.parent = self
        self.right = right
    def __str__(self):
        return str(self.id)


def preorder(arr, root, res):
    if root == None:
        return
    res.append(root)
    preorder(arr, root.left, res)
    preorder(arr, root.right, res)

def inorder(arr, root, res):
    if root == None:
        return
    inorder(arr, root.left, res)
    res.append(root)
    inorder(arr, root.right, res)

def postorder(arr, root, res):
    if root == None:
        return
    postorder(arr, root.left, res)
    postorder(arr, root.right, res)
    res.append(root)


def main():
    n = int(input())
    array = [Node(i) for i in range(n)]
    for node in array:
        i, l, r = list(map(int, input().split()))
        array[i].setLeft(array[l]) if l != -1 else None
        array[i].setRight(array[r]) if r != -1 else None
    
    root = None
    for node in array:
        if node.parent == None:
            root = node
            break

    res = []
    preorder(array, root, res)
    print("Preorder\n ", end="")
    print(*res) 
    res = [] 
    inorder(array, root, res)
    print("Inorder\n ", end="")
    print(*res)
    res = []
    postorder(array, root, res)
    print("Postorder\n ", end="")
    print(*res)
    
if __name__ == "__main__":
    main()

        

    

