def partition(arr, p, r):
    x = int(arr[r][1])
    i = p - 1
    for j in range(p, r):
        if int(arr[j][1]) <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)
def merge(arr, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [i for i in range(n1 + 1)]
    R = [i for i in range(n2 + 1)]
    for i in range(n1):
        L[i] = arr[left + i]
    for i in range(n2):
        R[i] = arr[mid + i]
    L[n1] = ['last', 10**9 + 1]
    R[n2] = ['last', 10**9 + 1]
    i = 0
    j = 0
    for k in range(left, right):
        if int(L[i][1]) <= int(R[j][1]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
def mergeSort(arr, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid, right)
        merge(arr, left, mid, right)
n = int(input())
a = [list(input().split()) for i in range(n)]
b = [i for i in a]
mergeSort(b, 0, n)
quickSort(a, 0, n - 1)
print('Stable' if a == b else 'Not stable')
for i in a:
    print(' '.join(i))
