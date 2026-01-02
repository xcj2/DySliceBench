import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()

class Heap(object):
    def __init__(self, A):
        self._heap = []
        # heapify は O(n) でできるらしいが、O(nlogn) で妥協
        # cf. https://github.com/python/cpython/blob/3.8/Lib/heapq.py
        for a in A:
            self.append(a)

    def __len__(self):
        return len(self._heap)

    def __bool__(self):
        return bool(self._heap)

    def front(self):
        assert self
        return self._heap[0]

    def append(self, x):
        self._heap.append(x)
        now = len(self)-1
        heap = self._heap
        # n の親は (n-1)//2
        while now!=0 and heap[now] < heap[(now-1)//2]:
            heap[now], heap[(now-1)//2] = heap[(now-1)//2], heap[now]
            now = (now-1)//2

    def pop(self):
        assert self
        if len(self)==1:
            return self._heap.pop()

        heap = self._heap
        res, heap[0] = heap[0], heap.pop()
        # n の子は 2*n+1, 2*n+2
        now = 0
        while(1):
            if now*2+1 >= len(self): break # 子が存在しない
            # 子がひとつだけのとき、必要なら入れ替えて終わり
            if now*2+1 == len(self)-1:
                if heap[now] > heap[now*2+1]:
                    heap[now], heap[now*2+1] = heap[now*2+1], heap[now]
                break
            # 子が複数のとき
            else:
                # 親、子1、子2のうち、親が最小であれば終わり
                if min(heap[now], heap[2*now+1], heap[2*now+2]) == heap[now]: break
                # そうでないとき、子のうち小さい方を親と入れ替える
                next = min((heap[2*now+1],2*now+1), (heap[2*now+2],2*now+2))[1]
                heap[now], heap[next] = heap[next], heap[now]
                now = next

        return res

    def sort(self):
        return [self.pop() for _ in range(len(self))]

def resolve():
    n, m = map(int,input().split())
    A = list(map(lambda x:-int(x),input().split()))
    heap = Heap(A)
    for _ in range(m):
        x = -heap.pop()
        x //= 2
        heap.append(-x)

    print(-sum(heap._heap))
resolve()