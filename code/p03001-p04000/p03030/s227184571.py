class MaxHeapInt(object):
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)


def resolve():
    import heapq
    from collections import defaultdict
    N = int(input())
    SS = []
    SP = defaultdict(list)
    for i in range(N):
        S, Pt = input().split()
        P = int(Pt)
        heapq.heappush(SS, S)
        heapq.heappush(SP[S], MaxHeapInt(P, i + 1))
    while len(SS) > 0:
        S = heapq.heappop(SS)
        while len(SP[S]) > 0:
            print(heapq.heappop(SP[S]).idx)


resolve()
