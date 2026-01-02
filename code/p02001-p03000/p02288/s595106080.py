def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    # 左の子、自分、右の子で値が最大のノードを選ぶ
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)


def left(i):
    return i*2


def right(i):
    return i*2 + 1


def buildMaxHeap(A):
    for i in range(H//2, 0, -1):
        maxHeapify(A, i)


H = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

buildMaxHeap(A)
print('', *A[1:])

