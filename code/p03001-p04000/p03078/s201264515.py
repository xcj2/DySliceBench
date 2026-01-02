from heapq import heapify, heappush, heappop


class AscKeyMappedPriorityQueue(object):

    def __init__(self, arr=None, key_generator=lambda x: x):
        """
        昇順以外のソートをheapqで実現することはできず、昇順になるキーを挿入する値から作る必要がある。
        tupleの扱いやらが面倒なのでオブジェクトとしてpush, pop操作を簡易に行えるようにしている。
        :param arr: ヒープ化する元の配列が存在する場合は指定する
        :param key_generator: 挿入する値から昇順になるようなキーを作る関数
        """
        self.key_generator = key_generator
        if arr:
            self.arr = [(key_generator(e), e) for e in arr]
            heapify(self.arr)
        else:
            self.arr = []

    def push(self, e):
        heappush(self.arr, (self.key_generator(e), e))

    def pop(self):
        return heappop(self.arr)[1]


X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
C = sorted(C, reverse=True)

considered = set()

q = AscKeyMappedPriorityQueue(key_generator=lambda v: (-v[0], v[1], v[2], v[3]))
q.push((A[0] + B[0] + C[0], 0, 0, 0))
considered.add((0, 0, 0))

for _ in range(K):
    e, a, b, c = q.pop()
    print(e)
    if not (a + 1, b, c) in considered and len(A) > a + 1:
        q.push((A[a + 1] + B[b] + C[c], a + 1, b, c))
        considered.add((a + 1, b, c))
    if not (a, b + 1, c) in considered and len(B) > b + 1:
        q.push((A[a] + B[b + 1] + C[c], a, b + 1, c))
        considered.add((a, b + 1, c))
    if not (a, b, c + 1) in considered and len(C) > c + 1:
        q.push((A[a] + B[b] + C[c + 1], a, b, c + 1))
        considered.add((a, b, c + 1))
