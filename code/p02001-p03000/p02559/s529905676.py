class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    
    def build(self, lis):
        self.value = lis
        for i, x in enumerate(lis):
            self.add(i+1, x)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    
    def get_sum(self, i, j):
        return self.sum(j) - self.sum(i)


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    bit = FenwickTree(n)
    bit.build(a)
    
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            bit.add(query[1]+1, query[2])
        else:
            print(bit.get_sum(query[1], query[2]))
    
    
if __name__ == "__main__":
    main()