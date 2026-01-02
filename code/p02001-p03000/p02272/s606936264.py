import sys

input = sys.stdin.readline

MAX = 500000
GUARD = 2000000000
cnt = 0

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid] + [MAX]
    R = A[mid:right] + [MAX]

    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    
    L[n1] = GUARD
    R[n2] = GUARD
    i = 0
    j = 0

    global cnt
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

def main():
    n = int(input())
    S = list(map(int, input().split()))

    mergeSort(S, 0, n)

    print(*S)
    print(cnt)
             
if __name__ == "__main__":
    main()
