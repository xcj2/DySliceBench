def maxHeapiify(A, i, n):
    l = 2*i+1
    r = 2*i+2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapiify(A, largest, n)


def buildMaxHeap(A, n):
    for i in range(n//2, -1, -1):
        maxHeapiify(A, i, n)


def main():
    N = int(input())
    H = list(map(int, input().split()))
    buildMaxHeap(H, N)
    print(" ", end="")
    print(*H)


if __name__ == '__main__':
    main()

