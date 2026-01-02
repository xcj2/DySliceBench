def height(cx, cy, D):
    for x, y, h in D:
        if h <= 0: continue
        return h + abs(x-cx) + abs(y-cy)
    return 0

def valid(cx, cy, H, D):
    for x, y, h in D:
        if h != max(H - abs(x-cx) - abs(y-cy), 0):
            return False
    return True

def solve():
    for cy in range(0, 101):
        for cx in range(0, 101):
            H = height(cx, cy, D)
            if valid(cx, cy, H, D):
                return (cx, cy, H)
    return (0, 0, 0)

N = int(input())
D = []
for i in range(N):
    x, y, h = map(int, input().split())
    D.append((x, y, h))
cx, cy, H = solve()
print(cx, cy, H)

