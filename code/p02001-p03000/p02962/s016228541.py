S = input()
W = input()
M = len(S)
S *= 3 * (len(W)//len(S)+1)


N = len(W)
def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret

def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)

D = divisors(N)
p = 1
for d in D:
    if W[:-d] == W[d:]:
        W = W[:d]
        p = N//d
        N = d
        break

W = W[:d]

T = [-1] * (len(W)+1)

ii = 2
jj = 0

T[0] = -1
T[1] = 0

while ii < len(W) + 1:
    if W[ii - 1] == W[jj]:
        T[ii] = jj + 1
        ii += 1
        jj += 1
    elif jj > 0:
        jj = T[jj]
    else:
        T[ii] = 0
        ii += 1
m = 0
def KMP(i0):
    global m, i
    ret = -1

    while m + i < len(S):
        if W[i] == S[m + i]:
            i += 1
            if i == len(W):
                t = m
                m = m + i - T[i]
                if i > 0:
                    i = T[i]
                return t
        else:
            m = m + i - T[i]
            if i > 0:
                i = T[i]
    return len(S)

i = 0
j = -10**9
c = 0
cmax = 0
f = 0
while m < len(S)-N:
    k = KMP(0)
    if k == len(S):
        break
    elif k == N + j:
        c += 1
    else:
        c = 1
        f += 1
    cmax = max(cmax, c)
    j = k
if f == 1:
    print(-1)
else:
    print(cmax//p)
