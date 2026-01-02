def left(num):
    return int(num*2)

def right(num):
    return int(num*2)+1

def maxHeapify(i, H):
    l = left(i)
    r = right(i)
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(largest, H)

def buildMaxHeap(H):
    for i in range(int(H/2), 0, -1):
        maxHeapify(i, H)

if __name__ == "__main__":
    H = int(input())
    A = [-1] + list(map(int, input().split()))
    buildMaxHeap(H)
    print(' ' + ' '.join(map(str, A[1:])))

