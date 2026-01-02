# Heaps - Complete Binary Tree
from math import floor

def parent(i):
    p_id = floor(i/2)
    if p_id > 0: return p_id
    else: return 0

def left(H,i):
    l_id = 2 * i
    if 0 < l_id < H: return l_id
    else: return 0

def right(H,i):
    r_id = 2 * i + 1
    if 0 < r_id < H: return r_id
    else: return 0

def build_max_heap(A):
    H = len(A)
    for i in range(H//2,0,-1):
        max_heapify(A,i)

def max_heapify(A,i):
    H = len(A)
    l = left(H,i)
    r = right(H,i)
    largest = 0
    if 1 <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    if not largest == i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

H = int(input())
heap = [-2000000001]*(H+1)
for i,k in enumerate(input().split()):
    heap[i+1] = int(k)

build_max_heap(heap)

for i,h in enumerate(heap):
    if i == 0: continue
    print(' {0}'.format(h), end='')
print()
