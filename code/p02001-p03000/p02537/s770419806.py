def segfunc(x, y): return max(x, y)
def update(i, x):
    i += MAX_N-1
    node[i] = x
    while i:
        i = (i-1)//2
        node[i] = segfunc(node[i*2+1], node[i*2+2])

def query(l, r):
    L = l + MAX_N
    R = r + MAX_N
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = segfunc(s, node[R - 1])
        if L & 1:
            s = segfunc(s, node[L - 1])
            L += 1
        L >>= 1
        R >>= 1
    return s

N, K = map(int, input().split())
MAX_N = 2**(300005).bit_length()
a = [int(input()) for _ in range(N)]
node = [0] * (2 * MAX_N)
INF = 0
ans = 0

#for i in range(N):
#    update(i, a[i])

for i in a:
    tmp = query(max(i - K, 0), min(300005, i + K) + 1)
    update(i, tmp + 1)
    ans = max(ans, tmp + 1)
print(ans)
