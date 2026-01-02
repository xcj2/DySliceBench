class MaxHeapInt(object):
    def __init__(self, val):  self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)


def resolve():
    import heapq
    n, Q = [int(i) for i in input().split()]
    ans = [[] for _ in range(n)]
    for _ in range(Q):
        q = [int(i) for i in input().split()]
        if q[0] == 0:
            heapq.heappush(ans[q[1]], MaxHeapInt(q[2]))
        elif q[0] == 1:
            if len(ans[q[1]]) > 0:
                print(ans[q[1]][0].val)
        else:
            if len(ans[q[1]]) > 0:
                heapq.heappop(ans[q[1]])


resolve()

