X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

from heapq import heapify, heappop, heappush, heappushpop
 
 
class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)
 
    def push(self, item):
        heappush(self.heap, item)
 
    def pop(self):
        return heappop(self.heap)
 
    def pushpop(self, item):
        return heappushpop(self.heap, item)
 
    def __call__(self):
        return self.heap
 
 
heap = []  # ヒープといっても順序を工夫したただのリスト
 
q = PriorityQueue(heap)
q.push((-(A[0] + B[0] + C[0]), 0, 0, 0))
 
considered = set()
ans = []
for k_th in range(1, K+1):
    heap_max, i, j, k = q.pop()
    ans.append(-heap_max)
    for di, dj, dk in zip([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        i_new, j_new, k_new = i + di, j + dj, k + dk
        if i_new >= X or j_new >= Y or k_new >= Z:
            continue
        if (i_new, j_new, k_new) in considered:
            continue
        considered.add((i_new, j_new, k_new))
        q.push((-(A[i_new] + B[j_new] + C[k_new]), i_new, j_new, k_new))
 
 
print(*ans, sep='\n')
