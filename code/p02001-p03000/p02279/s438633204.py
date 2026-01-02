#coding:utf-8

n = int(input())
T = [list(map(int, input().split())) for i in range(n)]
A = []
def parentSearch():
    numList = []
    for t in T:
        if t[1] != 0:
            for num in t[2:]:
                numList.append(num)
    numList.sort()
    for i in range(n-1):
        if numList[i] != i:
            return i


def rootedTrees(node, parent, depth):
    t = T[node]
    if t[1] != 0:
        if parent == -1:
            kind = "root"
        else:
            kind = "internal node"
        A.append([t[0], parent, depth, kind, t[2:]])
        parent = node
        for i in t[2:]:
            rootedTrees(i, parent, depth+1)
    else:
        if parent == -1:
            kind = "root"
        else:
            kind = "leaf"
        A.append([t[0], parent, depth, kind, []])


def Merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    L.append([510000])
    R.append([510000])
    i,j = 0,0
    for k in range(left,right):
        if L[i][0] <= R[j][0]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def MergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right)//2
        MergeSort(A, left, mid)
        MergeSort(A, mid, right)
        Merge(A, left, mid, right)

MergeSort(T, 0, n)
node = parentSearch()
if node == None:
    node = 0
depth = 0
parent = -1
rootedTrees(node, parent, depth)
MergeSort(A, 0, n)

for t in A:
    print("node {}: parent = {}, depth = {}, {}, {}".format(t[0],t[1],t[2],t[3],t[4]))
