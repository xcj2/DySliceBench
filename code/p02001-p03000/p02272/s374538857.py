import sys
input = sys.stdin.readline

n = int(input())
S = list(map(int, input().split()))
SENTINEL = 1000000005
merge_count = 0


def main():
    mergeSort(S, 0, len(S))
    print(' '.join(map(str, S)))
    print(merge_count)


def merge(A, left, mid, right):
    # print("---merge start---")
    # print("A is {}".format(A))
    # print("left:{0}, mid:{1}, right{2}".format(left, mid, right))
    global merge_count

    L = A[left:mid] + [SENTINEL]
    R = A[mid:right] + [SENTINEL]

    # print("L:{}".format(L))
    # print("R:{}".format(R))

    i, j = 0, 0
    for k in range(left, right, 1):
        merge_count += 1
        # print("k:{0}".format(k))
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    # print("A is {}".format(A))
    # print("----merge end----".format(A))


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        # print("------mergeSort start--------")
        # print("left:{0}, mid:{1}, right:{2}".format(left, mid, right))
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == '__main__':
    main()

