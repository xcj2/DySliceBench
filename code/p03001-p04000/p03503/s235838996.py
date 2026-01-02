def main():
    n = int(input())
    f = []
    for _ in range(n):
        x = [int(s) for s in input().split()]
        p = 0
        for y in x:
            p <<= 1
            p |= y
        f.append(p)
    p = [[int(s) for s in input().split()] for _ in range(n)]
    print(solve(n, f, p))

def solve(n, f, p):
    m = float('-inf') 
    for i in range(1, 1024):
        q = 0
        for j in range(n):
            c = ones(f[j] & i)
            q += p[j][c]
        m = max(m, q)
    return m

def ones(n):
    m = 0
    while n != 0:
        if n & 0x01 != 0:
            m += 1
        n >>= 1
    return m

main()
