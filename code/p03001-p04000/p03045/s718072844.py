def solve(string):
    n, m, *xyz = map(int, string.split())
    t = [-1] * (n + 1)
    for x, y, z in zip(*[iter(xyz)] * 3):

        def union(r1, r2):
            new_root = min(r1, r2)
            if r1 != r2:
                t[max(r1, r2)] = new_root

        def find(x):
            if t[x] < 0:
                return x
            t[x] = find(t[x])
            return t[x]

        union(find(x), find(y))
    return str(t[1:].count(-1))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m)])))
