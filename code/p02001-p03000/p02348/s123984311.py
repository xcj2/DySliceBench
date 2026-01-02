import sys
readline = sys.stdin.readline
write = sys.stdout.write
n, q = map(int, readline().split())
 
N0 = 2**(n-1).bit_length()
data = [None]*(2*N0)
INF = (-1, 2**31-1)

def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = v
 
        if L & 1:
            data[L-1] = v
            L += 1
        L >>= 1; R >>= 1
        
def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s
def query(k):
    return _query(k)[1]
 
 
ans = []
for i in range(q):
    t, *cmd = map(int, readline().split())
    if t:
        ans.append(str(query(cmd[0])))
    else:
        s, t, x = cmd
        update(s, t+1, (i, x))
        
write("\n".join(ans))
write("\n")
