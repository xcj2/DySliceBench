import sys
input = sys.stdin.readline

def parent(i):
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i+1

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
        A[i], A[largest] = A[largest], A[i] # pythonはこれで要素の入れ替えが可能
        maxHeapify(A, largest)

def buildMaxHeap(A, H):
    for i in range(H//2, 0, -1):
        maxHeapify(A, i)

H = int(input())
A = [None] + list(map(int, input().split()))

buildMaxHeap(A, H)

print(' ' + ' '.join(map(str, A[1:])))
