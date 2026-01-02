from collections import deque

def pow_two_more_than(a):
    # print(a, a & (a - 1), bin(a), 1 << (len(bin(a))-2))
    if (a & (a - 1)) == 0:
        return a
    # print(1 << (len(bin(a))-2))
    return 1 << (len(bin(a))-2)

class SegmentTree:
    def __init__(self, n, l):
        self.n = pow_two_more_than(n)
        self.tree = [2**31-1]*self.n + l + [2**31-1]*(self.n-len(l))
        for i in reversed(range(1, self.n)):
            self.update_one_node(i)

    def update(self, index, m):
        x = self.n+index
        self.tree[x] = m
        while x >= 1:
            x //= 2
            self.update_one_node(x)
        # print(self.tree)
    
    def find(self, rl, rr):
        # print(f"find: [{rl}, {rr})")
        # print(self.tree[self.n:])
        min_num = 2**31-1
        q = deque([1])
        c = 0
        while q:
            # print(q)
            t = q.popleft()
            # print(t)
            height = len(bin(t)) - 3
            x = t ^ (1<<height)
            w = (self.n>>height)
            l, r = w*x, w*(x+1)
            # print((l, r), height, end=" ")
            if rl <= l and r <= rr:
                # print("complatly in")
                min_num = min(min_num, self.tree[t])
            elif r <= rl or rr <= l:
                pass
                # print("out")
            else:
                # print((l, r), (rl, rr))
                # print("overlap")
                for c in self.get_childs(t):
                    if c < self.n*2:
                        q.append(c)
            c += 1
        # print(c)
        return min_num

    def update_one_node(self, m):
        self.tree[m] = min(self.tree[c] for c in self.get_childs(m))

    # def update(self)

    def get_childs(self, m):
        return [2*m, 2*m+1]

N, Q = map(int, input().split())
CXY = [list(map(int, input().split())) for _ in range(Q)]
# N, Q = 10**5, 10**5
# CXY = [[0, i, i] for i in range(Q//2)] + [[1, 0, 0] for i in range(Q-Q//2)]

segtree = SegmentTree(N, [2**31-1]*N)

for c, x, y in CXY:
    if c == 0:
        segtree.update(x, y)
    else:
        x, y = x, y+1
        r = segtree.find(x, y)
        print(r)
