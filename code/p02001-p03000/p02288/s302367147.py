import sys
input = sys.stdin.readline

def maxHeapify(A: list, i: int):
    H = len(A) - 1
    l = 2 * i
    r = l + 1
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)
    return

def buildMaxHeap(A: list):
    H = len(A) - 1
    for i in range(H//2, 0, -1):
        maxHeapify(A, i)
    return

def main():
    H = int(input())
    A = [0] + list(map(int, input().split()))
    buildMaxHeap(A)
    for i in range(1, H+1):
        print(' {}'.format(A[i]), end='')
    print()

if __name__ == '__main__': main()
