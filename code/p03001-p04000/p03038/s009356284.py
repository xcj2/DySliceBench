import heapq
import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N, M = tuple(li())
A = list(li())
heapq.heapify(A)
def update(pq, k, val):
    # update pq in place
    for _ in range(k):
        cur = heapq.heappop(pq)
        if cur < val:
            heapq.heappush(pq, val)
        else:
            heapq.heappush(pq, cur)
            break

ops = []
# val, k_sum
keep = dict()
for i in range(M):
    k, val = tuple(li())
    k_sum = keep.get(val, 0)
    keep[val] = k_sum + k

for val, k in keep.items():
    update(A, k, val)

print(sum(A))
