# coding: utf-8

def getList(H, W, A):
    rList = [0] * H
    cList = [0] * W
    for r in range(H):
        for c in range(W):
            if A[r][c] == "#":
                rList[r] += 1
                cList[c] += 1
    return rList, cList

def getTargetList(tList):
    zeroList = []
    for i in range(len(tList)):
        if tList[i] == 0:
            zeroList.append(i)
    return zeroList
    
def delRow(A, tList):
    for r in reversed(tList):
        A.pop(r)
    return A

def delCol(A, tList):
    for c in reversed(tList):
        for r in range(len(A)):
            A[r].pop(c)
    return A

def solve(H, W, A):
    rList, cList = getList(H, W, A)
    A = delRow(A, getTargetList(rList))
    A = delCol(A, getTargetList(cList))
    return A
    
if __name__ == "__main__":
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        tmp = input()
        A.append([])
        for s in tmp:
            A[i].append(s)

    A = solve(H, W, A)
    for i in A:
        for j in i:
            print(j, end="")
        print()
