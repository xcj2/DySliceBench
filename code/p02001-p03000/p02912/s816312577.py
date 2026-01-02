class SegmentTree:
    def __init__(self, value, N=0, comp=lambda x,y: x<=y, reverse=False):
        M = max(len(value),N)
        N = 2**(len(bin(M))-3)
        if N < M: N *= 2
        self.N = N
        self.node = [0] * (2*N-1)
        for i in range(N):
            self.node[N-1+i] = i
        self.value = [None] * N
        for i, v in enumerate(value):
            self.value[i] = v
        self.comp = lambda x, y: True if y is None else False if x is None else comp(x,y)^reverse
        for i in range(N-2,-1,-1):
            left_i, right_i = self.node[2*i+1], self.node[2*i+2]
            left_v, right_v = self.value[left_i], self.value[right_i]
            self.node[i] = left_i if self.comp(left_v, right_v) else right_i

    def update(self, n, v):
        self.value[n] = v
        i = (self.N-1) + n
        while i > 0:
            i = (i-1)//2
            left_i, right_i = self.node[2*i+1], self.node[2*i+2]
            left_v, right_v = self.value[left_i], self.value[right_i]
            new_i = left_i if self.comp(left_v, right_v) else right_i
            if new_i == self.node[i] and new_i != n:
                break
            else:
                self.node[i] = new_i

    def at(self, n):
        if n is None:
            return None
        else:
            return self.value[n]

    def query(self, l=0, r=-1):
        return self.at(self.query_index(l,r))

    def query_index(self, l=0, r=-1):
        if r < 0: r = self.N
        L = l + self.N; R = r + self.N
        s = None
        while L < R:
            if R & 1:
                R -= 1
                if self.comp(self.at(self.node[R-1]), self.at(s)):
                    s = self.node[R-1]
            if L & 1:
                if self.comp(self.at(self.node[L-1]), self.at(s)):
                    s = self.node[L-1]
                L += 1
            L >>= 1; R >>= 1
        return s

inpl = lambda: list(map(int,input().split()))

if __name__ == '__main__':
    N, M = inpl()
    A = inpl()
    segt = SegmentTree(A, reverse=True)
    for _ in range(M):
        i = segt.query_index()
        v = segt.at(i)
        segt.update(i, v//2)
    print(sum(segt.at(i) for i in range(N)))