import sys
import copy
input = sys.stdin.readline

n = int(input())
# カードの番号だけintにcastしながら受け取る
A = [None for _ in range(n)]
M = [None for _ in range(n)]
for i in range(n):
    tmp = list(input().split())
    A[i] = [tmp[0], int(tmp[1])]
    M[i] = [tmp[0], int(tmp[1])]

# mergeSortで使う
SENTINEL = 1000000005
merge_count = 0


def main():
    # print("before sort:{}".format(A))
    quickSort(A, 1, len(A) - 1)
    # print("quickSort Result:{}".format(A))
    mergeSort(M, 0, len(M))
    # print("mergeSort Result:{}".format(M))

    print(isStable(A, M))
    for a in A:
        print(a[0] + ' ' + str(a[1]))


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def partition(A, p, r):
    last = A[r][1]
    i = p - 1
    # print("last:{}".format(last))
    # print("i:{}".format(i))
    for j in range(i, r, 1):
        # print("A[j]:{}".format(A[j]))
        if A[j][1] <= last:
            # print("change")
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1

        # print(A)
    tmp = A[i]
    A[i] = A[r]
    A[r] = tmp

    return i


def merge(M, left, mid, right):
    # print("---merge start---")
    # print("M is {}".format(M))
    # print("left:{0}, mid:{1}, right{2}".format(left, mid, right))
    global merge_count

    L = M[left:mid] + [["SENTINEL", SENTINEL]]
    R = M[mid:right] + [["SENTINEL", SENTINEL]]

    # print("L:{}".format(L))
    # print("R:{}".format(R))

    i, j = 0, 0
    for k in range(left, right, 1):
        merge_count += 1
        # print("k:{0}".format(k))
        if L[i][1] <= R[j][1]:
            M[k] = L[i]
            i += 1
        else:
            M[k] = R[j]
            j += 1

    # print("M is {}".format(M))
    # print("----merge end----")


def mergeSort(M, left, right):
    # print("------mergeSort start--------")
    # print("left:{0}, right:{1}".format(left, right))

    if left + 1 < right:
        mid = (left + right) // 2
        # print("left:{0}, mid:{1}, right:{2}".format(left, mid, right))
        mergeSort(M, left, mid)
        mergeSort(M, mid, right)
        merge(M, left, mid, right)


def isStable(A, M):
    for i in range(len(A)):
        if A[i] != M[i]:
            return "Not stable"
    return "Stable"


if __name__ == '__main__':
    main()

