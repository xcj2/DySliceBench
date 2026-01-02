#  --*-coding:utf-8-*--

MAX = 10000

def makeMap(H, bits):
    M = [0]*H

    m = 0
    for i in range(H):
        M[i] = m

        if bits & 1:
            m += 1

        bits >>= 1

    return M


def getCounts(H,S,M,w):
    C = [0]*(M[-1]+1)

    for h in range(H):
        if S[h][w] == '1':
            C[M[h]] += 1

    return C


def f(H,W,K,S,bits):
    M = makeMap(H, bits)
    N = M[-1] + 1
    X = [0]*N
    ans = 0
    
#    print("M", M)

    for w in range(W):
        C = getCounts(H,S,M,w)
        for i in range(N):
            if C[i] > K:
                return MAX

            X[i] += C[i]
            if X[i] > K:
                ans += 1
                X = C
                break
#        print("X", X, ans)

#    print("ans", ans, ans + N - 1)
    return ans + N - 1
            
    
H,W,K = map(int, input().split())
S = [input() for _ in range(H)]

# print(S)

ans = MAX

for bits in range(2**(H-1)):
    ans = min(ans, f(H,W,K,S,bits))

print(ans)
