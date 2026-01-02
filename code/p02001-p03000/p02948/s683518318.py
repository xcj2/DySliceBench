import sys
input = sys.stdin.readline
inpl = lambda: list(map(int,input().split()))

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
            if self.comp(left_v, right_v):
                self.node[i] = left_i
            else:
                self.node[i] = right_i

    def set_input(self, n, v):
        self.value[n] = v
        i = (self.N-1) + n
        while i > 0:
            i = (i-1)//2
            left_i, right_i = self.node[2*i+1], self.node[2*i+2]
            left_v, right_v = self.value[left_i], self.value[right_i]
            if self.comp(left_v, right_v):
                new_i = left_i
            else:
                new_i = right_i
            if new_i == self.node[i] and new_i != n:
                break
            else:
                self.node[i] = new_i

    def get_input(self, n):
        if n is None:
            return None
        else:
            return self.value[n]

    def get_output(self, a=0, b=-1):
        return self.get_input(self.get_output_index(a,b))

    def get_output_index(self,
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
            left_i = self.get_output_index(a,b,2*k+1,l,(l+r)//2)
            right_i = self.get_output_index(a,b,2*k+2,(l+r)//2,r)
            left_v, right_v = self.get_input(left_i), self.get_input(right_i)
            if left_v is None and right_v is None:
                return None
            elif self.comp(left_v, right_v):
                return left_i
            else:
                return right_i

N, M = inpl()
AB = [ inpl() for _ in range(N) ]
AB.sort()
A = [ ab[0] for ab in AB ]
B = [ ab[1] for ab in AB ]
sg = SegmentTree(B, reverse=True)
ans = 0
n = 0
for m in range(1,M+1):
    while n < N and A[n] <= m:
        n += 1
    p = sg.get_output_index(0, n)
    if p is not None:
        ans += sg.get_input(p)
        sg.set_input(p, None)
print(ans)