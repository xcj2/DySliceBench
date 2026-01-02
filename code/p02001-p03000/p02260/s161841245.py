def selection_sort(array):
    for i in range(len(array)):
        j = min(range(i, len(array)), key=lambda x: array[x])
        array[i], array[j] = array[j], array[i]


class SegmentTree(object):

    def __init__(self, size, op=min, init=float("inf")):
        self.size = 1
        self.op = op
        self.init = init
        while self.size < size:
            self.size *= 2
        self.data = [init] * (self.size*2+2)

    def update(self, idx, value):
        k = idx + self.size - 1
        self.data[k] = value
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self.op(self.data[k*2+1], self.data[k*2+2])

    def __getitem__(self, val):
        return self.data[(self.size-1)+val]

    def find(self, start, end):
        def query(k, left, right):
            if right <= start or end <= left:
                return self.init
            if start <= left and right <= end:
                return self.data[k]
            vl = query(k*2+1, left, (left+right)//2)
            vr = query(k*2+2, (left+right)//2, right)
            return self.op(vl, vr)
        return query(0, 0, self.size)


def swap_count(array):
    count = 0
    rmq = SegmentTree(len(array), op=min, init=(float("inf"), float("inf")))
    for i, v in enumerate(array):
        rmq.update(i, (v, i))
    for i in range(len(array)):
        vi, _ = rmq[i]
        vj, idx = rmq.find(i, len(array))
        j = idx
        if rmq[i] <= rmq[j]:
            continue
        count += 1
        rmq.update(i, (vj, i))
        rmq.update(j, (vi, j))
    return count

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(*sorted(A))
    count = swap_count(A)
    print(swap_count(A))