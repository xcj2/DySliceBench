def get_item(L,i): return L[i] if len(L) > i else -2*10**9-1
def left (i): return i*2
def right(i): return i*2 + 1

def maxHeapify(A,i):
    l = left(i)
    r = right(i)
    largest = i
    if get_item(A,l) > A[largest]: largest = l
    if get_item(A,r) > A[largest]: largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i] 
        maxHeapify(A, largest)


def buildMaxHeap(A):
    for i in range(len(A)//2,0,-1): maxHeapify(A,i)


if __name__=='__main__':
    H = int(input())
    hp = [0] + list(map(int,input().split()))
    buildMaxHeap(hp)
    print("",*hp[1:])