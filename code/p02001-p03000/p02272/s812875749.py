count = 0

def Merge(arr, left, mid, right):

    global count

    inf = 10000000000
    n1 = mid - left
    n2 = right - mid
    L = arr[left:left + n1] + [inf]
    R = arr[mid:mid + n2] + [inf]

    i = j = 0

    for k in range(left, right):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            count += 1      
        else:
            arr[k] = R[j]
            j += 1
            count += 1
            
def MergeSort(arr, left, right):
    if (left + 1) < right:
        mid = int((left + right)/2)
        MergeSort(arr, left, mid)
        MergeSort(arr, mid, right)
        Merge(arr, left, mid, right)

def Main():
    n = int(input())
    arr = [int(a) for a in input().split()]

    MergeSort(arr, 0, n)

    print(*arr)
    print(count)

Main()
