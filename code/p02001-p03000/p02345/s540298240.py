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
 

if __name__ == "__main__":
    n, q = list(map(int, input().split()))
    tree = SegmentTree(n, init=(1<<31)-1)
    for _ in range(q):
        com, x, y = list(map(int, input().split()))
        if com == 0:
            tree.update(x, y)
        else:
            print(tree.find(x, y+1))