import sys
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
 
 
def main():
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def mi():    return map(int, input().split())
    def lmi():   return list(map(int, input().split()))
    
 
    class MaxPQueue:
        def __init__(self):
            self.h = []
            self.size = 0
 
        def is_empty(self):
            return self.size == 0
        
        def push(self, delicious_dq):
            self.size += 1
            heappush(self.h, list(map(lambda x: -x, delicious_dq)))
        
        def pop(self):
            self.size -= 1
            tmp = heappop(self.h)
            return list(map(lambda x: -x, tmp)) 
 
 
    n, k = mi()
    L = [lmi() for _ in range(n)]
    L.sort(key=lambda x: x[1], reverse=True)
 
    d = dict()
    for neta, delcious in L:
        if neta in d:
            d[neta].append(delcious)
        else:
            d[neta] = [delcious]
 
    group_num = dict()
    group_size = 0
    ans = 0
    for neta, delcious in L[:k]:
        ans += delcious
        if neta in group_num:
            group_num[neta] += 1
        else:
            group_num[neta] = 1
            group_size += 1
    ans += group_size ** 2
    
    pq_new = MaxPQueue()
    for neta in d.keys():
        if neta not in group_num:
            pq_new.push(d[neta])
    
    # print(L)
    # print(ans)
    # print(group_num)
    prev = ans
    for ind in range(k-1, -1, -1):
        neta, delicious = L[ind]
        if group_num[neta] > 1 and not pq_new.is_empty():
            diff = pq_new.pop()[0] + (2 * group_size + 1) - delicious
            ans = max(ans, prev + diff)
            prev += diff
            group_size += 1
            group_num[neta] -= 1
            # print(f"prev {prev}")            
    print(ans)
 
 
 
if __name__ == "__main__":
    main()