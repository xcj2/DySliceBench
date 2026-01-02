def MAX(a, b):
    return b + (((((a + ms - b) & ms) >> (K - 1)) * tt) & (ms + a - b))
def MIN(a, b):
    return a - (((((a + ms - b) & ms) >> (K - 1)) * tt) & (ms + a - b))

def tolist(n):
    sx = bin(n)[2:] + "_"
    return [int(sx[-(i+1) * K - 1:-i * K - 1], 2) for i in range((len(sx)+K-2) // K)]

K = 52
N, W = map(int, input().split())

ms = int(("1" + "0" * (K - 1)) * (W + 1), 2)
tt = (1 << K - 1) - 1
one = int(("0" * (K - 1) + "1") * (W + 1), 2)

a = 8
b = 39

s = 1 << K - 2 + (W * K)
for _ in range(N):
    w, v = map(int, input().split())
    s = MAX(s, (s >> w * K) + one * v)

print(max(tolist(s)) - (1 << K - 2))