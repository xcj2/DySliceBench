class binaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

n = int(input())
root = None
for index in range(n):
    inputL = input().split()
    if inputL[0] == 'insert':
        if index == 0:
            root = binaryTreeNode(int(inputL[1]))
        else:
            def walkNode(node, val, parent):
                if node != None:
                    if node.val > val:
                        walkNode(node.left, val, node)
                    else:
                        walkNode(node.right, val, node)
                else:
                    if parent.val > val:
                        parent.left = binaryTreeNode(val)
                    else:
                        parent.right = binaryTreeNode(val)
            walkNode(root, int(inputL[1]), None)
    else:
        inL = [] 
        def lookNodeIn(node):
            if node != None:
                lookNodeIn(node.left)
                inL.append(node.val)
                lookNodeIn(node.right)
        lookNodeIn(root)
        preL = []
        def lookNodePre(node):
            if node != None:
                preL.append(node.val)
                lookNodePre(node.left)
                lookNodePre(node.right)
        lookNodePre(root)
        print(' '+' '.join(list(map(str, inL))))
        print(' '+' '.join(list(map(str, preL))))
