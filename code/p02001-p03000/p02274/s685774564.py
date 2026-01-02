inv_count = 0

def Merge(A, left, mid, right):
    global inv_count

    sentinel = 2000000000
    n1 = mid - left
    n2 = right - mid
    L = A[left : left + (mid - left)] + [sentinel] 
    R = A[mid : mid + (right - mid)] + [sentinel]
    i = 0
    j = 0

    for k in range(left, right):
        if L[i] <= R[j] :
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inv_count += (n1 - i)

def MergeSort(A, left, right):

    if left + 1 < right :
        mid = int((left + right)/2)
        MergeSort(A, left, mid)
        MergeSort(A, mid, right)
        Merge(A, left, mid, right)

def Main():
    N = input()
    A = [int(a) for a in input().split()]
    MergeSort(A, 0, len(A))
    global inv_count
    print(inv_count)

Main()
