inf = 10000000000

def partition(a, left, right):
    pivot = a[right - 1]
    i = left - 1
    for j in range(left, right - 1):
        if a[j][1] <= pivot[1]:            
            i = i + 1
            A[i], A[j] = A[j], A[i]
            
    A[i + 1], A[right - 1] = A[right - 1], A[i + 1]
    return i + 1

def quick_sort(a, left, right):
    if left < right:
        q = partition(a, left, right)
        quick_sort(a, left, q)
        quick_sort(a, q + 1, right)

def merge(a, left, mid, right):
    L = a[left : mid] + [('jorker', inf)]
    R = a[mid : right] + [('jorker', inf)]
    i = j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1


def merge_sort(a, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)

    

if __name__ == "__main__":
    n = int(input())
    A = [None] * n
    B = [None] * n
    for i in range(n):
        picture, number = input().split()
        A[i] = (picture, int(number))
        B[i] = (picture, int(number))
    
    quick_sort(A, 0, n)
    merge_sort(B, 0, n)

    if A == B:
        print('Stable')
    else:
        print('Not stable')

    for a in A:
        print(a[0], a[1])
    


