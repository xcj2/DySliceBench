def main():
    n = int(input())
    vs = [int(s) for s in input().split()]

    print(solve(vs))

def solve(vs):
    c1 = count(vs[0::2])
    c2 = count(vs[1::2])

    a1 = c1[0]
    a2 = c1[1] if len(c1) > 1 else (0, 0)
    b1 = c2[0]
    b2 = c2[1] if len(c2) > 1 else (0, 0)

    if a1[0] != b1[0]:
        return len(vs) - a1[1] - b1[1]

    if a1[1] + b2[1] > a2[1] + b1[1]:
        return len(vs) - a1[1] - b2[1]
    else:
        return len(vs) - a2[1] - b1[1]

def count(vs):
    c = dict()

    for v in vs:
        c[v] = c.get(v, 0) + 1

    cs = sorted(c.items(), key=lambda x: x[1], reverse=True)
    return cs

main()
