def merge(cnt, A, left, mid, right):
    L = A[left:mid] + [1e+99]
    R = A[mid:right] + [1e+99]
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    cnt.append(right - left)

            
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

print(*S)
print(sum(cnt))

