def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N = INT()
ans = [0] * N

def fn(x, y, z):
    f = x**2 + y**2 + z**2 + x * y + y * z + z * x
    return f

for x in range(1, int(N ** 0.5) + 2):
    if fn(x, 1, 1) > N:
        break
    for y in range(1, int(N ** 0.5) + 2):
        if fn(x, y, 1) > N:
            break
        for z in range(1, int(N ** 0.5) + 2):
            f = fn(x, y, z)
            if f > N:
                break
            if f <= N:
                ans[f - 1] += 1

for a in ans:
    print(a)