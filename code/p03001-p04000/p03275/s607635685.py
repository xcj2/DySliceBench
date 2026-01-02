N = int(input())
a = [int(i) for i in input().split()]

half = ((N * (N + 1) // 2) + 1) // 2

class BinaryIndexedTree() :
    def __init__(self, N) :
        self.N = N
        self.tree = [0] * (N + 1)
        
    def sum(self, i) :
        s = 0
        while i > 0 :
            s += self.tree[i]
            i -= i & -i
        return s
        
    def add(self, i, x) :
        while i <= self.N :
            self.tree[i] += x
            i += i & -i

def check(x) :
    b = [0] + [1 if a[i] >= x else -1 for i in range(N)]
    for i in range(1, N + 1) :
        b[i] += b[i-1]
    BIT = BinaryIndexedTree(2*N+2)
    
    ret = 0
    for i in range(N+1) :
        ret += BIT.sum(N+1+b[i])
        BIT.add(N+1+b[i], 1)
    
    return ret >= half
    
aa = sorted(a)
ok = 0
ng = N
while ng - ok > 1 :
    mid = (ok + ng) // 2
    if check(aa[mid]) :
        ok = mid
    else :
        ng = mid

print(aa[ok])
    