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
        if root == None:
            root = binaryTreeNode(int(inputL[1]))
        else:
            def insertN(node, val, parent):
                if node != None:
                    if node.val > val:
                        insertN(node.left, val, node)
                    else:
                        insertN(node.right, val, node)
                else:
                    if parent.val > val:
                        parent.left = binaryTreeNode(val)
                    else:
                        parent.right = binaryTreeNode(val)
            insertN(root, int(inputL[1]), None)
    elif inputL[0] == 'print':
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
    
    else:
        def searchNode(node, val):
            if node != None:
                if node.val == val:
                    return 'yes'
                else:
                    if node.val > val:
                        return searchNode(node.left, val)
                    else:
                        return searchNode(node.right, val)
            return 'no'
        print(searchNode(root, int(inputL[1])))

