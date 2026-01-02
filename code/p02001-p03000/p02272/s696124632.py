INF = 2*int(1e9)
cnt = 0
def merge(A, left, mid, right):
    global cnt
    nl = mid - left
    nr = right - mid
    L = A[left:mid]
    R = A[mid:right]
    L.append(INF)
    R.append(INF)
    i = 0
    j = 0
    for k in range(left, right):
        cnt = cnt +  1
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i +  1
        else:
            A[k] = R[j]
            j = j + 1


def mergeSort(A, left, right):
    if left+1<right:
        mid = (left+right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

def main():
    n = int(input())
    s = [int(i) for i in input().split()]
    mergeSort(s, 0, n)
    for i in range(n):
        if i == n-1:
            print(s[i])
        else:
            print(s[i], end=' ')

    print(cnt)
main()
