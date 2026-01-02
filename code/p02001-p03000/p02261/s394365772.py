import sys
input = sys.stdin.readline
import copy

class trump:
    def __init__(self, s):
        self.name = s
        s = list(s)
        self.value = int(s[1])

N=int(input())
C = list(map(trump, input().split()))
C_copy = C.copy()

def BubbleSort(A,N):
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if A[j].value < A[j-1].value:
                A[j],A[j-1]=A[j-1],A[j]
    for i in range(N):
        if i==N-1:
            print(A[i].name)
        else:
            print(A[i].name,end=" ")
    print("Stable")

def SelectionSort(A,N):
    for i in range(N):
        minj=i
        for j in range(i,N):
            if A[j].value<A[minj].value:
                minj=j
        A[i],A[minj]=A[minj],A[i]
    for i in range(N):
        if i==N-1:
            print(A[i].name)
        else:
            print(A[i].name,end=" ")
    if C==C_copy:
        print("Stable")
    else:
        print("Not stable")
        
BubbleSort(C,N)
SelectionSort(C_copy,N)

