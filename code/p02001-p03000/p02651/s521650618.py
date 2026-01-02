from heapq import heappush, heappop


def calcSpace():
    H = []
    hpush = lambda x: heappush(H, -x)
    hpop = lambda: -heappop(H)
    for x in X:
        hpush(x)
    
    E = [0] * 60
    while H:
        x = hpop()
        b = x.bit_length() - 1
        if E[b]:
            x ^= E[b]
            if x: hpush(x)
        else:
            E[b] = x
    
    return E
    
def chk(y):
    y0 = y
    for i in range(60)[::-1]:
        if y >> i & 1:
            if V[i]:
                y ^= V[i]
                # print("chk", y0, "OK", V)
                if y == 0: return 1
            else:
                return 0

def chk_all():
    for y in Y:
        if chk(y) == 0:
            return 1
            break
    else:
        return 0
    
T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) for a in input().split()]
    S = [int(a) for a in input()]
    
    if 0:
        print("N =", N)
        print("A =", A)
        print("S =", S)
    
    X = []
    Y = []
    i = N - 1
    ans = 0
    while i >= 0:
        while i >= 0:
            if S[i]: break
            X.append(A[i])
            i -= 1
        while i >= 0:
            if S[i] == 0: break
            Y.append(A[i])
            i -= 1

            V = calcSpace()
            # print("X =", X)
            # print("Y =", Y)
            # print("V =", V)
            if chk_all():
                ans = 1
                i = -1
    print(ans)