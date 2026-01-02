class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

N = int(input())
b_sum = 0
Q1 = []
Q = []
vars = []
for _ in range(N):
    Qu = list(map(int, input().split()))
    Q.append(Qu)
    if Qu[0]==1:
        _, a, b = Qu
        vars.append(a)
        #b_sum += b
    else:
        pass
vars = list(set(vars))
vars.sort()
d = dict((v, i) for i, v in enumerate(vars))
lend = len(d)
bit = Bit(lend)
bit2 = Bit(lend)
n = 0
for q in Q:
    if q[0]==1:
        _, a, b = q
        bit.add(d[a], a)
        bit2.add(d[a], 1)
        b_sum += b
        n += 1
    else:
        l, r = 0, len(vars)
        con = (n - 1) >> 1
        while l+1 < r:
            c = (l+r)>>1
            cnt = bit2.sum(c)
            if cnt <= con:
                l = c
            else:
                r = c
        idx = l
        v = vars[idx]
        m = bit2.sum(idx)
        s = bit.sum(idx)
        m_ = bit2.sum(lend) - m
        s_ = bit.sum(lend) - s
        ans = b_sum + m*v-s + s_-m_*v
        print(v, ans)
