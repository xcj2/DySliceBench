# coding: utf-8
# Your code here!

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        

def bubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0;
        for i in reversed(range(1, N)):
            if A[i-1].value > A[i].value:
                A[i-1], A[i] = A[i] , A[i-1]
                flag = 1;
    showResult(A)
    return A

def selectionSort(A, N):
    for i in range(0, N):
        minj = i
        mink = i
        for j in range(i, N):
            if A[mink].value > A[j].value:
                mink = j
        if minj != mink:
            A[minj], A[mink] = A[mink], A[minj]
    showResult(A)
    return A



def showResult(B):
    for i in range(N-1):
        print(B[i].suit+str(B[i].value), end = " ")
    print(B[N-1].suit+str(B[N-1].value))

def isStable(rawA, sortedA):
    rawDic = listToDic(rawA)
    sortedDic = listToDic(sortedA)
    flag = 1
    for key in rawDic:
        if len(rawDic[key]) >= 2:
            for i in range(len(rawDic[key])-1):
                if rawDic[key][i] != sortedDic[key][i]:
                    
                    flag = 0
    if flag:
        print("Stable")
    else:
        print("Not stable")

def listToDic(raw):
    rawDic = {}
    for i in range(len(raw)):
        if rawDic.get(raw[i].value) != None:
            rawDic[raw[i].value].append(raw[i].suit)
        else:
            rawDic[raw[i].value] = [raw[i].suit]
    return rawDic

N = int(input())
A = list(input().split()) 
B = []
for i in range(0, N):
    B.append(Card(A[i][:1], A[i][1:]))
C = tuple(B)
"""
C = []
for i in range(0, N):
    C.append(Card(A[i][:1], A[i][1:]))
D = []
for i in range(0, N):
    D.append(Card(A[i][:1], A[i][1:]))
E = []
for i in range(0, N):
    E.append(Card(A[i][:1], A[i][1:]))

F = tuple(B)
print(B)
"""

bubbleA = bubbleSort(B.copy(), N)
isStable(B.copy(), bubbleA)
selectionA = selectionSort(B.copy(), N)
isStable(B.copy(), selectionA)





