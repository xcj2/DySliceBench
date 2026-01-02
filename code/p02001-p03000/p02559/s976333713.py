import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,q = list(map(int, input().split()))

### BIT binary
def init(bit, values):
    for i,v in enumerate(values):
        add(bit,i+1,v)
#a1 ~ aiまでの和 O(logn)
def query(bit,i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i&(-i)
    return res

#ai += x(logN)
def add(bit,i,x):
    if i==0:
        raise RuntimeError
    while i <= len(bit)-1:
        bit[i] += x
        i += i&(-i)
    return

def index(bit, v):
    """a1,...,aiの和がv以上になる最小のindexを求める
    存在しないとき配列サイズを返す
    """
    i = 0
    n = len(bit)-1
    k = 1<<((n-1).bit_length())
    while k>0:
        if i+k<n+1 and bit[i+k]<v:
            v -= bit[i+k]
            i += k
        k //= 2
    if v==1:
        return i+1
    else:
        return n+1
bit = [0]*(n+1)    
init(bit, list(map(int, input().split())))
for i in range(q):
    t,u,v = map(int, input().split())
    if t==0:
        add(bit, u+1, v)
    else:
        print(query(bit, v) - query(bit, u))