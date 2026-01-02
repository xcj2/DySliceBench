cnt = 0
def merge(A, left, mid, right):
    global cnt
    L = A[left:mid]
    R = A[mid:right]
    L.append(float("inf"))
    R.append(float("inf"))
    i, j = 0, 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left+right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

def solve(A):
    left = 0
    right = len(A)
    mergeSort(A, left, right)

def resolve():
    n = int(input())
    A = [int(i) for i in input().split()]
    solve(A)
    print(*A)
    print(cnt)

resolve()

