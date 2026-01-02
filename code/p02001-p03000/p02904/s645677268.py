inpl = lambda: list(map(int,input().split()))

INF = 2**31-1
class SegmentTree:
    def __init__(self, value, N=0, comp=lambda x,y: x<=y, reverse=False):
        M = max(len(value),N)
        N = 2**(len(bin(M))-3)
        if N < M: N *= 2
        self.N = N
        self.node = [0] * (2*N-1)
        self.reverse = reverse
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

#    def get_output(self, a=0, b=-1):
#        return self.get_input(self.get_output_index(a,b))

    def get_output(self, l, r):
        L = l + self.N; R = r + self.N
        if self.reverse:
            s = -INF
        else:
            s = INF
        while L < R:
            if R & 1:
                R -= 1
                if self.reverse:
                    s = max(s, self.value[self.node[R-1]]) 
                else:
                    s = min(s, self.value[self.node[R-1]])

            if L & 1:                    
                if self.reverse:
                    s = max(s, self.value[self.node[L-1]])
                else:
                    s = min(s, self.value[self.node[L-1]])
                L += 1
            L >>= 1; R >>= 1
        return s

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

def get_sequence(arr):
    if len(arr) == 0:
        return [], []
    elements = []
    nums = []
    n = 1
    prev = arr[0]
    for c in arr[1:]:
        if c == prev:
            n += 1
        else:
            elements.append(prev)
            nums.append(n)
            prev = c
            n = 1
    elements.append(prev)
    nums.append(n)
    return elements, nums

N, K = inpl()
P = inpl()
minseg = SegmentTree(P)
maxseg = SegmentTree(P, reverse=True)

ans = 1
for i in range(N-K):
    if P[i] < minseg.get_output(i+1,i+K) and P[i+K] > maxseg.get_output(i+1,i+K):
        pass
    else:
        ans += 1

ordered = [ P[i] < P[i+1] for i in range(N-1)]
elements, nums = get_sequence(ordered)
nums = nums[(elements[0]+1)%2::2]

unchanged = len(list(filter(lambda x: x>=K-1, nums)))
if unchanged > 1:
    ans -= unchanged-1

print(ans)