class binaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

n = int(input())
hashMap = {}
rootL = list(range(n))
for index in range(n):
    inputL = list(map(int, input().split()))
    if not inputL[0] in hashMap:
        hashMap[inputL[0]] = binaryTreeNode(inputL[0])
    parent = hashMap[inputL[0]]
    if inputL[1] != -1:
        rootL.remove(inputL[1])
        if not inputL[1] in hashMap:
            hashMap[inputL[1]] = binaryTreeNode(inputL[1])
        parent.left = hashMap[inputL[1]]
    if inputL[2] != -1:
        rootL.remove(inputL[2])
        if not inputL[2] in hashMap:
            hashMap[inputL[2]] = binaryTreeNode(inputL[2])
        parent.right = hashMap[inputL[2]]

root = hashMap[rootL[0]]
print('Preorder')
preL = []
def lookNodePre(node):
    if node != None:
        preL.append(node.val)
        lookNodePre(node.left)
        lookNodePre(node.right)
lookNodePre(root)
print(' '+' '.join(list(map(str, preL))))

print('Inorder')
InL = []
def lookNodeIn(node):
    if node != None:
        lookNodeIn(node.left)
        InL.append(node.val)
        lookNodeIn(node.right)
lookNodeIn(root)
print(' '+' '.join(list(map(str, InL))))

print('Postorder')
postL = []
def lookNodePost(node):
    if node != None:
        lookNodePost(node.left)
        lookNodePost(node.right)
        postL.append(node.val)
lookNodePost(root)
print(' '+' '.join(map(str, postL)))
