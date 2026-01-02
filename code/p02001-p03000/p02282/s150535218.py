class Node:
    def __init__(self, no):
        self.no = no
        self.parent = -1
        self.left = self.right = -1
    def postorder(self):
        global t
        L = []
        if self.left >= 0: L += t[self.left].postorder()
        if self.right >= 0: L += t[self.right].postorder()
        L.append(self.no)
        return L

def makeTree(parent, preList, inList):
    global t
    if preList == []:
        return -1
    root = preList[0]
    t[root].parent = parent
    index = inList.index(root)
    t[root].left = makeTree(root, preList[1:index+1], inList[:index])
    t[root].right = makeTree(root, preList[index+1:], inList[index+1:])
    return root

n = int(input())
t = [ Node(i) for i in range(n+1) ]
preList = list(map(int, input().split()))
inList = list(map(int, input().split()))
root = makeTree(-1, preList, inList)
print(*t[root].postorder())

