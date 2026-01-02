n = int(input())
nums = list(map(int,input().split(" ")))
nodes = []

class Node():
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def defineParent(self,parent):
        self.parent = parent

    def defineLeft(self,left):
        self.left = left

    def defineRight(self,right):
        self.right = right

def heapify(nums,parentIndex,root):
    leftIndex = parentIndex*2+1
    rightIndex = parentIndex*2+2
    rightFlag = False
    leftFlag = False
    if leftIndex < len(nums):
        leftNode = Node(nums[leftIndex])
        root.left = leftNode
        leftNode.parent = root
        nodes[leftIndex] = leftNode
        leftFlag = True
    if rightIndex < len(nums):
        rightNode = Node(nums[rightIndex])
        root.right = rightNode
        rightNode.parent = root
        nodes[rightIndex] = rightNode
        rightFlag = True
    if leftFlag:
        heapify(nums,leftIndex,leftNode)
    if rightFlag:
        heapify(nums,rightIndex,rightNode)

def doIt(l):
    leftIndex = 2*l+1
    rightIndex = 2*l+2
    vsNodes = [nodes[l].value]
    nextIndex = []
    if leftIndex < len(nodes):
        nextIndex.append(leftIndex)
        vsNodes.append(nodes[leftIndex].value)
    if rightIndex < len(nodes):
        nextIndex.append(rightIndex)
        vsNodes.append(nodes[rightIndex].value)
    maximumValue = max(vsNodes)
    if maximumValue > nodes[l].value:
        if maximumValue == nodes[leftIndex].value:
            changeIndex = leftIndex
        elif maximumValue == nodes[rightIndex].value:
            changeIndex = rightIndex
        tmp = nodes[l]
        nodes[l] = nodes[changeIndex]
        nodes[changeIndex] = tmp
        doIt(changeIndex)

def maxHeapify(nodes):
    startIndex = len(nodes)//2
    for l in range(startIndex,-1,-1):
        doIt(l)


nodes = [None]*len(nums)
treeRoot = Node(nums[0])
nodes[0] = treeRoot
heapify(nums,0,treeRoot)

#初期化は成功

flag = True
while flag:
    flag = maxHeapify(nodes)

ans = ""
for i in nodes:
    ans += " " + str(i.value)

print(ans)

