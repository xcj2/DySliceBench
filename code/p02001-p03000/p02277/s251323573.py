# coding: utf-8
# Your code here!
import copy

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value



def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = []
    R = []
    for i in range(n1):
        L.append(A[left + i])
    for i in range(n2):
        R.append(A[mid + i])
    L.append(Card("", 2000000000))
    R.append(Card("", 2000000000))
    
    i = 0
    j = 0
    
    for k in range(left, right):
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) // 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
        
        





def partition(A, p, r):
    x = A[r - 1].value
    i = p - 1
    for j in range(p, r - 1):
        if A[j].value <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r -1] = A[r -1], A[i + 1]
    return i + 1
        
        
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q)
        quickSort(A, q + 1, r)
    return
    
    

n = int(input())
A = []
for i in range(n):
    tmp = list(input().split())
    A.append(Card(tmp[0], int(tmp[1])))

B = copy.copy(A)
flg = True

quickSort(A, 0, n)
mergeSort(B, 0, n)

for i in range(n):
    if A[i].suit != B[i].suit:
        flg = False
if flg:
    print("Stable")
else:
    print("Not stable")
        
for i in range(n):
    print(A[i].suit, A[i].value)







