import heapq

class ErasableHeapq:
    def __init__(self):
        self.p = list()
        self.q = list()
        self.len = 0

    def insert(self, x):
        heapq.heappush(self.p, x)
        self.len += 1
        return

    def erase(self, x):
        heapq.heappush(self.q, x)
        self.len -= 1
        return

    def minimum(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return self.p[0]

    def __len__(self):
        return self.len

    def empty(self):
        return self.len == 0

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 大きい順
    A.sort()
    sA = A[::-1]

    ans = sA[0]

    eq = ErasableHeapq()
    eq.insert((-sA[1], -sA[0]))
    eq.insert((-sA[1], -sA[0]))

    for a in sA[2:]:
        best_pair = eq.minimum()
        eq.erase(best_pair)
        # print(a, best_pair)
        ans += -best_pair[0]
        eq.insert((-a, best_pair[0]))
        eq.insert((-a, best_pair[1]))

    print(ans)

if __name__ == '__main__':
    main()