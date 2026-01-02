H, W = map(int, input().split())
I = [input() for _ in range(H)]
X = [[[0, 1][a=="#"] for a in inp] for inp in I]
k = 32
def r():
    global H, W, I
    I = ["".join([I[H - 1 - j][i] for j in range(H)]) for i in range(W)]
    H, W = W, H
def st1(s):
    return int(s.replace("#", "1" * k).replace(".", "0" * k), 2)
def st2(s):
    return int(s.replace("#", "0" * (k - 1) + "1").replace(".", "0" * k), 2)
def getsum(x):
    for i in range(8):
        x += x >> (k << i)
    return x & ((1 << k) - 1)

ans = 0
for _ in range(4):
    A1 = [st1(inp) for inp in I]
    A2 = [st1("".join([I[i][j] for i in range(H)])) for j in range(W)]
    B = [st2(inp[::-1]) for i, inp in enumerate(I)]
    C = [[0] * W for _ in range(H)]
    for j in range(W):
        s = 0
        m = (1 << j * k) - 1
        for i in range(H)[::-1]:
            s <<= k
            s += B[i] >> (j+1) * k
            s &= m
            C[i][j] = s
    for i in range(1, H):
        for j in range(1, W):
            ans += A1[i] >> (W - j) * k & A2[j] >> (H - i) * k & C[i][j]
    r()
            
print(getsum(ans))