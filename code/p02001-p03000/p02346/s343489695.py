from array import array

class BIT(object):

    def __init__(self, size, init_data=None):
        self.size = size
        if init_data is None:
            init_data = [0] * (size + 1)
        self.data = array("q", init_data)

    def sum(self, idx):
        ret = 0
        while idx > 0:            
            ret += self.data[idx]
            idx -= idx & -idx # idx = idx & (idx - 1)
        return ret

    def add(self, idx, value):
        while idx <= self.size:
            self.data[idx] += value
            idx += idx & -idx

if __name__ == "__main__":
    n, q = list(map(int, input().split()))
    bit = BIT(n)
    for _ in range(q):
        com, x, y = list(map(int, input().split()))
        if com == 0:
            bit.add(x, y)
        else:
            print(bit.sum(y)-bit.sum(x-1))