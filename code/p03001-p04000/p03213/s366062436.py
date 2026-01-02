def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def count(n):
    t = {}
    while n != 1:
        for p in P:
            while n % p == 0:
                t[p] = t.setdefault(p, 0) + 1
                n //= p
    return t


def p_count(N):
    T = {}
    for n in range(1, N + 1):
        if n in P:
            T[n] = T.setdefault(n, 0) + 1
            continue
        
        t = count(n)
        for k, v in t.items():
            T[k] = T.setdefault(k, 0) + v
    return T


def main():
    N = int(input())
    T = p_count(N)
    L = sorted([t for t in T.keys() if T[t] >= 2])
    res = 0
    q = set()
    for i1, t1 in enumerate(L):
        for i2, t2 in enumerate(L[i1 + 1:]):
            for i3, t3 in enumerate(L[i1 + i2 + 2:]):
                if T[t2] >= 4 and T[t3] >= 4:
                    q.add((t1 ** 2) * (t2 ** 4) * (t3 ** 4))
                    res += 1
                if T[t1] >= 4 and T[t3] >= 4:
                    q.add(t1 ** 4 * t2 ** 2 * t3 ** 4)
                    res += 1
                if T[t1] >= 4 and T[t2] >= 4:
                    q.add(t1 ** 4 * t2 ** 4 * t3 ** 2)
                    res += 1

    for p, c1 in T.items():
        for q, c2 in T.items():
            if p == q:
                continue

            if c1 >= 2 and c2 >= 24:
                res += 1

            if c1 >= 4 and c2 >= 14:
                res += 1

    res += len([t for t in T.keys() if T[t] >= 74])

    print(res)


if __name__ == "__main__":
    main()
