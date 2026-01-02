N = int(input())
P = list(map(int,input().split()))

order = [None] * N
for i,p in enumerate(P):
    order[p-1] = i

bit = [0] * (N+2)
def bit_add(x,w):
    while x <= N+1:
        bit[x] += w
        x += (x & -x)
def bit_sum(x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= (x & -x)
    return ret

def bisect_right(k):
    def is_ok(i):
        if i < 1: return True
        if i > N+1: return False
        return bit_sum(i) <= k
    ok = 0
    ng = N+2
    while ng-ok > 1:
        m = (ok+ng) // 2
        if is_ok(m):
            ok = m
        else:
            ng = m
    return ok

ans = 0
for q,i in enumerate(reversed(order)):
    bit_add(i+2, 1)
    #print([bit_sum(i) for i in range(1,N+2)])
    k = bit_sum(i+2)
    a = bisect_right(k-3)
    b = bisect_right(k-2)
    c = bisect_right(k-1)
    d = bisect_right(k)
    e = bisect_right(k+1)
    ans += ((b-a)*(d-c) + (c-b)*(e-d)) * (N-q)
print(ans)