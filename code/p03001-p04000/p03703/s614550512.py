class BIT():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for i in range(N+1)]
    def add(self, a, w):
        x = a
        while 1:
            self.bit[x] += w
            x += x & -x
            if x > self.N:
                break
    def sum(self, a):
        ret = 0
        x = a
        while 1:
            ret += self.bit[x]
            x -= x & -x
            if x <= 0:
                break
        return ret
    
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}

N, K = map(int, input().split())
a = []
B = []
sum_a = 0
for i in range(N):
    a_ = int(input())
    a.append(a_)
    sum_a += a_
    B.append(sum_a - K*(i+1))

B_C = compress(B)
ans = sum([1 for i in B if i >= 0])
B = [B_C [i]+1for i in B] # 1-indexed

N = max(B)
f_tree = BIT(N)
for i in B:
    ret = f_tree.sum(i)
    f_tree.add(i, 1)
    ans += ret
print(ans)