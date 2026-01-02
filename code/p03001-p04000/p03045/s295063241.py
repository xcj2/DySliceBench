def solve(string):
    n, m, *xyz = map(int, string.split())
    t = [-1] * (n + 1)
    for x, y, z in zip(*[iter(xyz)] * 3):

        def update(x, y):
            r1, p1 = x
            r2, p2 = y
            new_root = min(r1, r2)
            if r1 != r2:
                p2.append(max(r1, r2))
            for p in p1:
                t[p] = new_root
            for p in p2:
                t[p] = new_root

        def get_root(x):
            path = [x]
            curr = t[x]
            while curr != -1:
                path.append(curr)
                curr = t[curr]
            root = path.pop()
            return root, path

        update(get_root(x), get_root(y))
    return str(t[1:].count(-1))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m)])))
