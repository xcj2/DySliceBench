N = int(input())
S = input()
Q = int(input())
QUERY = [input().split() for _ in range(Q)]
# N = 4
# S = "abcd"
# QUERY = [s.split() for s in [
#     "2 1 4", # 4
#     "2 1 3", # 3
#     "2 3 4", # 2
#     "2 4 4", # 1
#     "1 2 a", # aacd
#     "2 1 2", # 1
#     "2 1 3", # 2
# ]]
# Q = len(QUERY)

def or_more_pow_two(n):
    if (n & (n-1)) == 0:
        return n
    return 1<<(len(bin(n))-2)

class SegmentTree:
    def __init__(self, n, l):
        self.n = or_more_pow_two(n)*2
        self.tree = [0]*self.n
        for i, l_i in enumerate(l):
            self.tree[self.n//2+i] = l_i
        for i in reversed(range(1, self.n//2)):
            self.node_update(i)
            # print(self.tree[i])

    # 1-indexed: [l, r)
    def find(self, l, r, fl=1, fr="self.n//2+1", node=1):
        if fr == "self.n//2+1":
            fr = self.n//2+1
        # print(f"find: ({l}, {r}), ({fl}, {fr}), {node}")
        if l <= fl and fr <= r:
            # print("in", bin(self.tree[node])[2:])
            return self.tree[node]
        elif fr <= l or r <= fl:
            # print("out")
            return 0
        else:
            # print("overlap")
            mid = (fl+fr)//2
            a = self.find(l, r, fl=fl, fr=mid, node=2*node)
            b = self.find(l, r, fl=mid, fr=fr, node=2*node+1)
            return a | b

    def update(self, index, v):
        # print("update:", index, v)
        x = self.n//2+index-1
        self.tree[x] = v
        while x > 0:
            x >>= 1
            self.node_update(x)

    def node_update(self, index):
        # print(index, [2*index, 2*index+1], list(map(bin, [self.tree[2*index], self.tree[2*index+1], self.tree[2*index] | self.tree[2*index+1]])))
        self.tree[index] = self.tree[2*index] | self.tree[2*index+1]

def char_to_bit(c):
    i = ord(c) - 97
    return (1 << i)
def bit_to_type_count(b):
    # print(bin(b)[2:])
    r = bin(b)[2:].count("1")
    # print(r)
    return r
# def bit_to_char(b):
#     for i in range(26):


segtree = SegmentTree(N, map(char_to_bit, S))

for t, *query in QUERY:
    t = int(t)
    if t == 1:
        i, c = query
        i, c = int(i), c
        segtree.update(i, char_to_bit(c))
    elif t == 2:
        l, r = map(int, query)
        l, r = l, r+1
        r = segtree.find(l, r)
        r = bit_to_type_count(r)
        print(r)
    # print(list(map(bin, segtree.tree)))
