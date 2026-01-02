inpl = lambda: list(map(int,input().split()))
class SegmentTree:
    def __init__(self, value, N=0, comp=lambda x,y: x<=y):
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
        self.comp = lambda x, y: True if y is None else False if x is None else comp(x,y)
        for i in range(N-2,-1,-1):
            left_i, right_i = self.node[2*i+1], self.node[2*i+2]
            left_v, right_v = self.get_value(left_i), self.get_value(right_i)
            if self.comp(left_v, right_v):
                self.node[i] = left_i
            else:
                self.node[i] = right_i

    def set_value(self, n, v):
        self.value[n] = v
        i = (self.N-1) + n
        while i > 0:
            i = (i-1)//2
            left_i, right_i = self.node[2*i+1], self.node[2*i+2]
            left_v, right_v = self.get_value(left_i), self.get_value(right_i)
            if self.comp(left_v, right_v):
                new_i = left_i
            else:
                new_i = right_i
            if new_i == self.node[i] and new_i != n:
                break
            else:
                self.node[i] = new_i

    def get_value(self, n):
        return self.value[n]

    def get_min(self, a=0, b=-1):
        return self.value[self.get_min_index(a,b)]

    def get_min_index(self,
                     a=0, b=-1,
                     k=0, l=0, r=-1):
        if b < 0:
            b = self.N
        if r < 0:
            r = self.N
        if a <= l and r <= b:
            return self.node[k]
        elif r <= a or b <= l:
            return None
        else:
            left_i = self.get_min_index(a,b,2*k+1,l,(l+r)//2)
            right_i = self.get_min_index(a,b,2*k+2,(l+r)//2,r)
            left_v, right_v = self.get_value(left_i), self.get_value(right_i)
            if self.comp(left_v, right_v):
                return left_i
            else:
                return right_i

N = int(input())
partners = []
orders = [0]*N
for i in range(N):
    partners.append(set())
for i in range(N-1):
    a, b = inpl()
    a -= 1
    b -= 1
    partners[a].add(b)
    partners[b].add(a)
    orders[a] += 1
    orders[b] += 1
sg = SegmentTree(orders)
C = sorted(inpl())
D = [0]*N
M = 0
# print(sg.value, sg.node)
for i in range(N-1):
    k = sg.get_min_index()
    D[k] = C[i]
    M += C[i]
    for p in partners[k]:
        partners[p].remove(k)
        sg.set_value(p, sg.get_value(p)-1)
        # print(sg.value,sg.node)
    sg.set_value(k, None)
    # print(sg.value,sg.node)
k = sg.get_min_index()
D[k] = C[N-1]

print(M)
print(' '.join(map(str,D)))