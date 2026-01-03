import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


H, W = MI()

pieces = H * W


memo = dict()
def divide(h, w):
    if memo.get((h, w)) is not None:
        return memo[(h, w)]
    elif memo.get((w, h)) is not None:
        return memo[(w, h)]
    p = h * w
    if w > 1:
        a1 = w // 2 * h
        a2 = p - a1
        memo[(h, w)] = (a1, a2)
    if h > 1:
        b1 = h // 2 * w
        b2 = p - b1
        if memo.get((h, w)) is not None:
            a1, a2 = memo[(h, w)]
            if abs(a1 - a2) > abs(b1 - b2):
                memo[(h, w)] = (b1, b2)
    return memo[(h, w)]


ans = float('inf')
for i in range(1, W):
    p1 = i * H
    p2, p3 = divide(W - i, H)
    ans = min(ans, max(p1, p2, p3) - min(p1, p2, p3))
for i in range(1, H):
    p1 = i * W
    p2, p3 = divide(H - i, W)
    ans = min(ans, max(p1, p2, p3) - min(p1, p2, p3))
print(ans)
