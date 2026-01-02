import copy

"""
クイックソートを構成する
"""
def partition(A, p, r):
    x = int(A[r][1])
    i = p-1 
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
        else:
            pass 
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


"""
マージソートを実装する
"""
def merge(A, left, mid, right):
    n1 = mid-left
    n2 = right-mid

    L = [[0, 0]]*(n1+1)
    for i in range(n1):
        L[i] = A[left+i]
    
    R = [[0, 0]]*(n2+1)
    for i in range(n2):
        R[i] = A[mid+i]
    
    L[n1][1] = 10000000000
    R[n2][1] = 10000000000

    i, j = 0, 0 
    for k in range(left, right):
        if int(L[i][1]) <= int(R[j][1]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    
def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left+right)//2
        #sortする
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        #統合する
        merge(A, left, mid ,right)


#------------------------------------------------
n = int(input())
card = [input().split() for i in range(n)]

copy_card = copy.copy(card)
quickSort(copy_card, 0, n-1)
quick_list = copy_card

copy_card = copy.copy(card)
mergeSort(copy_card, 0, n)
merge_list = copy_card

if quick_list == merge_list:
    print('Stable')
else:
    print('Not stable')
for i in range(n):
    print(' '.join(quick_list[i]))




