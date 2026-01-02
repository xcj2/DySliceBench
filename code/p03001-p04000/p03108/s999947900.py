def find(i, m):
    if m[i] < 0:
        return i
    return find(m[i], m)


def count(i, m):
    if m[i] < 0:
        return abs(m[i])
    return count(m[i], m)


def main():
    n, m, *ab = map(int, open(0).read().split())
    ab = ab[::-1]
    tmp = n * (n - 1) // 2
    utl = []
    par = [-1] * (n + 1)

    for u, v in zip(ab[::2], ab[1::2]):
        if find(u, par) == find(v, par):
            utl.append(tmp)
        else:
            i, j = find(u, par), find(v, par)
            utl.append(tmp)
            tmp -= par[i] * par[j]
            if par[i] > par[j]:
                i, j = j, i
            par[i] += par[j]
            par[j] = i

    ans = '\n'.join(map(str, utl[::-1]))
    print(ans)


if __name__ == '__main__':
    main()
