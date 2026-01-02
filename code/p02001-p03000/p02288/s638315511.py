import sys
readline = sys.stdin.readline
write = sys.stdout.write

err = -2 * (10**9) + 1

class Node:
    def __init__(self, k, l, r, p):
        self.key = k
        self.left = l
        self.right = r
        self.parent = p

def maxHeapify(A, i):
    l = 2*i #index of left child
    r = 2*i + 1 #right child
    H = len(A)-1 #heap size, A[0] is not used therefore -1
    largest = 0
    if l <= H and A[i].key < A[l].key:
        largest = l
    else:
        largest = i
    if r <= H and A[largest].key < A[r].key:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxHeapify(A, largest)

def buildmaxHeap(A):
    H = len(A)-1
    s = int(H/2)
    for i in range(s, 0, -1):
        maxHeapify(A, i)

n = int(input())
keys = list(map(int, readline().split()))

Heap = [Node(err, None, None, None) for i in range(n+1)]
for i in range(1, n+1):
    Heap[i].key = keys[i-1]
    if 2*i  < n+1:
        Heap[i].left = Heap[2*i]
    if 2*i + 1 < n+1:
        Heap[i].right = Heap[2*i + 1]
    if i > 1:
        Heap[i].parent = Heap[int(i/2)]
buildmaxHeap(Heap)
for i in range(1, n+1):
    write(" " + str(Heap[i].key))
write("\n")
