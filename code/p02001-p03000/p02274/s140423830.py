def merge(cnt, A, left, mid, right):
    L = A[left:mid] + [2147483648]
    R = A[mid:right] + [2147483648]
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            cnt.append(j)
        else:
            A[k] = R[j]
            j += 1
            
def mergeSort(cnt, A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        mergeSort(cnt, A, left, mid)
        mergeSort(cnt, A, mid, right)
        merge(cnt, A, left, mid, right)
        
        
import sys
def input():
    return sys.stdin.readline()[:-1]
    
n = int(input())
S = list(map(int, input().split()))

from collections import deque
cnt = deque()
mergeSort(cnt,S,0,n)

print(sum(cnt))
