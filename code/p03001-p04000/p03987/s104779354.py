import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
d = {}
for i,num in enumerate(a):
    d[num] = i+1
ans = 0

### BIT 
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

# a1,...,aiの和がv以上になる最小のindexを求める
def index(bit, v):
    i = 0
    k = 1
    n = len(bit)-1
    while 2*k<n:
        k *= 2
    while k>0:
        if i+k<n+1 and bit[i+k]<v:
            v -= bit[i+k]
            i += k
        k //= 2
    return i+1
bit = [0] * (n+2)
bit[n+1] = 1
for num in range(1,n+1):
    v = query(bit, d[num])
    v1 = index(bit, v) if v>0 else 0
    v2 = index(bit, v+1)
    ans += num * (d[num]-v1) * (v2 - d[num])
#     print(num, d[num], v1, v2, v, bit)
    add(bit, d[num], 1)
print(ans)