def main():
    n, m = map(int, input().split())
    s = []

    for _ in range(m):
        r = [int(x) for x in input().split()]
        s.append(r[1:])
    
    p = [int(s) for s in input().split()]

    print(solve(m, n, s, p))

def solve(m, n, s, p):
    c = 0
    for bits in range(2 ** n):
        for i in range(m):
            if not check(bits, s[i], p[i]):
                break
        else:
            c += 1
    return c

def check(bits, si, pi):
    n = 0
    for sij in si:
        if bits & (1 << (sij - 1)):
            n += 1
    
    if n % 2 == pi:
        return True

    return False


main()
