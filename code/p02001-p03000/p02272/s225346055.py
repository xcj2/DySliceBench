def merge_jibun(A, left, mid, right):
    L = A[left:mid] + [1000000]
    R = A[mid:right] + [1000000]
    # L.append(1000000)
    # R.append(1000000)

    i = 0
    j = 0
    global count
    
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_hoka(A, left, mid, right):
    global count
    inf = 10 ** 9
    L = A[left:mid] + [inf]
    R = A[mid:right] + [inf]
 
    i = 0
    j = 0
    for k in range(left, right):
        count += 1
        # print(L)
        # print(R)
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        # merge_jibun(A, left, mid, right)
        merge_hoka(A, left, mid, right)

n = int(input())
A = list(map(int, input().split()))
count = 0
mergeSort(A, 0, n)

print(' '.join(list(map(str, A))))
print(count)
