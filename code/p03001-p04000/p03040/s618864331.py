import sys
input = sys.stdin.readline
Q = int(input())
Y = []
D = []
S = [0] * Q
s = 0
for i in range(Q):
    a = list(map(int, input().split()))
    Y.append(a)
    if a[0] == 1:
        D.append(a[1])
        s += a[2]
    S[i] = s

D = sorted(list(set(D)))
INV = {}
for i in range(len(D)):
    INV[D[i]] = i

N = 17
X = [0] * (2**(N+1)-1)
C = [0] * (2**(N+1)-1)

def add(j, x):
    i = 2**N + j - 1
    while i >= 0:
        X[i] += x
        C[i] += 1
        i = (i-1) // 2

def rangeof(i):
    s = (len(bin(i+1))-3)
    l = ((i+1) - (1<<s)) * (1<<N-s)
    r = l + (1<<N-s)
    return (l, r)

def rangesum(a, b):
    l = a + (1<<N)
    r = b + (1<<N)
    s = 0
    while l < r:
        if l%2:
            s += X[l-1]
            l += 1
        if r%2:
            r -= 1
            s += X[r-1]
        l >>= 1
        r >>= 1
    return s
def rangecnt(a, b):
    l = a + (1<<N)
    r = b + (1<<N)
    s = 0
    while l < r:
        if l%2:
            s += C[l-1]
            l += 1
        if r%2:
            r -= 1
            s += C[r-1]
        l >>= 1
        r >>= 1
    return s

c = 0
su = 0
CC = [0] * (2**N)
for i in range(Q):
    y = Y[i]
    if y[0] == 1:
        add(INV[y[1]], y[1])
        CC[INV[y[1]]] += 1
        c += 1
        su += y[1]
    else:
        l, r = 0, 2**N
        while True:
            m = (l+r)//2
            rc = rangecnt(0, m)
            if rc >= (c+1)//2:
                r = m
            elif rc + CC[m] <= (c-1)//2:
                l = m
            else:
                break
        rs = rangesum(0, m)
        print(D[m], D[m]*rc-rs+(su-rs)-(c-rc)*D[m]+S[i])
