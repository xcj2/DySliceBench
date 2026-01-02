N, *A = map(int, open(0).read().split())
P = [-e for e in set(A)]
P.sort()
P.append(1)
MP = {e: i for i, e in enumerate(P)}
N += 1

data = [0]*(N+1)
def get(k):
    r = 0
    while k:
        r += data[k]
        k -= k & -k
    return r
def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k
N0 = 2**(N-1).bit_length()
def lower_bound(x):
    w = i = 0
    k = N0
    while k:
        if i+k <= N and w + data[i+k] <= x:
            w += data[i+k]
            i += k
        k >>= 1
    return i+1

for a in A:
    j = MP[-a]
    i = lower_bound(get(j+1))
    if i != N+2:
        add(i, -1)
    add(j+1, 1)
print(get(N))