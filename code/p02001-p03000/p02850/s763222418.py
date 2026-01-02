from sys import setrecursionlimit
setrecursionlimit(100000)

n = int(input())
arr = []

for i in range(n-1):
    S = input()
    ar = [int(s) for s in S.split(" ")]
    arr.append(ar)

def prepare(n, arr):
    data = [[] for i in range(n)]
    nodeStates = [-1 for i in range(n)]
    childNums = [0 for i in range(n)]

    for ar in arr:
        start = ar[0] - 1
        to = ar[1] - 1
        data[start].append(to)
        data[to].append(start)
    return data, nodeStates, childNums


data, nodeStates, childNums = prepare(n, arr)
mmk = {}
def generateID(start,to):
    if start < to:
        start,to = to, start

    return start * 100000 + to

def dfs(currentNode, arr, x):
    childNodes = arr[currentNode]
    nodeStates[currentNode] = 1
    childNums[currentNode] = len(childNodes)
    kk = 0
    for ch in childNodes:
        if nodeStates[ch] == -1:
            kk = kk + 1
            if kk == x:
                kk = kk + 1
            mmk[generateID(currentNode+1,ch+1)] = kk
            dfs(ch, arr, kk)

dfs(0, data, -1)
print(max(childNums))
for ar in arr:
    start = ar[0]
    to = ar[1]
    print(mmk[generateID(start,to)])


