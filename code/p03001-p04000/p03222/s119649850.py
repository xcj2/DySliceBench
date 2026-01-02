import sys
mod = pow(10, 9) + 7
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NNN = (10**2)
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, NNN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


def erabu(aW):
    r = 0
    for i in range(aW // 2 + 1 + 1):
        sp = aW - (2*i -1)
        r += cmb(sp+i+1-1, sp, mod)
    return r

N, W, K = [int(x) for x in input().strip().split(" ")]
hasi = 0
cc = []
if W == 1:
    if K == 1:
        print(1)
    else:
        print(0)
    sys.exit()
elif W == 2:
    cccl = [1, 1]
    cc = [1, 1]
elif W == 3:
    cccl = [1, 1, 1]
    cc = [2, 1, 2]
elif W >= 4:
    aW = W - 1
    hW = aW - 2
    nhW = aW - 3
    cc = []
    cccl = []
    for w in range(W):
        nn = max(W - 1 - w - 1, 0)
        nnn = max((W - 1) - nn - 2, 0)
        if w == W -1:
            nnn += 1
        cc.append(erabu(nn) * erabu(nnn))
        cccl.append(erabu(nn) * erabu(nnn-1))

cccl[0] = 0
cccr = cccl[::-1]
d = [1] + [0 for x in range(W-1)]
for i in range(N):
    newd = []
    for j in range(W):
        newd.append(0)
        if j != 0:
            newd[j] = (newd[j] + (d[j-1] * cccl[j]) )% mod
        if j != W-1:
            newd[j] = (newd[j] + (d[j+1] * cccr[j])) % mod
        newd[j] = (newd[j] + (d[j] * cc[j])) % mod
    d = newd[:]

print(d[K-1])
