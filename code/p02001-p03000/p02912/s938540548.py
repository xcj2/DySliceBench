import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()

class Heap(object):
    def __init__(self, A):
        self._heap = A[:]
        # heapify in linear time
        for i in range((len(A))//2-1,-1,-1): self._descend(i)

    def __len__(self):
        return len(self._heap)

    def __bool__(self):
        return bool(self._heap)

    def _descend(self, i):
        heap = self._heap
        now = i
        # i の子は 2i+1, 2i+2
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

    def front(self):
        assert self
        return self._heap[0]

    def append(self, x):
        self._heap.append(x)
        now = len(self)-1
        heap = self._heap
        # i の親は (i-1)//2
        while now!=0 and heap[now] < heap[(now-1)//2]:
            heap[now], heap[(now-1)//2] = heap[(now-1)//2], heap[now]
            now = (now-1)//2

    def pop(self):
        assert self
        if len(self)==1: return self._heap.pop()
        res, self._heap[0] = self._heap[0], self._heap.pop()
        self._descend(0)
        return res

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