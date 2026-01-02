import bisect
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
kouzi = []
for _ in range(N):
    S, T, X = map(int, input().split())
    kouzi.append([X, S, T-1])
kouzi.sort(reverse = True)

human = [int(input()) for _ in range(Q)]
ans = [-1]*(Q+1)


N0 = 2**(Q-1).bit_length()
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
t = 0
for task in kouzi:
    t += 1
    x = task[0]
    l = bisect.bisect_left(human, task[1]-x)
    r = bisect.bisect_right(human, task[2]-x)
    if l == r:
        continue
    update(l, r, (t, x))

for i in range(Q):
    q = query(i)
    if q == 2147483647:
        print(-1)
    else:
        print(q)
