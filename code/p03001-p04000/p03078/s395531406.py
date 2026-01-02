# データ構造：ヒープ
import heapq
class heapque:
    def __init__(self, *args):
        self.que = []
        for arg in args:
            self.push(arg)
    def push(self, v):
        heapq.heappush(self.que, v)
    def pop(self):
        return heapq.heappop(self.que)

# 定数
INF = float("inf")
MOD = int(1e9 + 7)

# エントリーポイント
def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    a = sorted(A, reverse=True)
    b = sorted(B, reverse=True)
    c = sorted(C, reverse=True)
    heap = heapque((-(a[0] + b[0] + c[0]), (0, 0, 0)))
    used = {(0, 0, 0)}
    for _ in range(K):
        cur = heap.pop()
        print(-cur[0])

        ai, bi, ci = cur[1]
        ns = ((min(ai + 1, X - 1), bi, ci), (ai, min(bi + 1, Y - 1), ci), (ai, bi, min(ci + 1, Z - 1)))
        for n in ns:
            if n in used: continue
            heap.push((-(a[n[0]] + b[n[1]] + c[n[2]]), n))
            used |= {n}

main()
