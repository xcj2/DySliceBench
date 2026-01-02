# coding: utf-8

Node = list()
n = int(input())

def insertKey(k):
    idx = len(Node)
    Node.append([k, -1, -1])
    if idx > 0:
        pPrv = -1
        pTmp = 0
        while pTmp != -1:
            pPrv = pTmp
            if k < Node[pTmp][0]:
                pTmp = Node[pTmp][1]
            else:
                pTmp = Node[pTmp][2]
        if Node[-1][0] < Node[pPrv][0]:
            Node[pPrv][1] = idx
        else:
            Node[pPrv][2] = idx

def inOrder(num):
    if num == -1:
        return
    inOrder(Node[num][1])
    print(' {}'.format(Node[num][0]), end = '')
    inOrder(Node[num][2])

def preOrder(num):
    if num == -1:
        return
    print(' {}'.format(Node[num][0]), end = '')
    preOrder(Node[num][1])
    preOrder(Node[num][2])

for i in range(n):
    temp = input().strip()
    if temp[:6] == 'insert':
        insertKey(int(temp[7:]))
    else:
        inOrder(0)
        print('')
        preOrder(0)
        print('')
