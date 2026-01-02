def read_valus():
    return map(int, input().split())


def read_list():
    return list(read_valus())


def read_lists(N):
    return [read_list() for n in range(N)]


def main():
    N, M = read_valus()
    L = read_lists(N)

    F = [
        lambda l: l[0] + l[1] + l[2],
        lambda l: - l[0] + l[1] + l[2],
        lambda l: l[0] - l[1] + l[2],
        lambda l: l[0] + l[1] - l[2],
        lambda l: - l[0] - l[1] + l[2],
        lambda l: - l[0] + l[1] - l[2],
        lambda l: l[0] - l[1] - l[2],
        lambda l: - l[0] - l[1] - l[2],
    ]

    res = 0
    for f in F:
        T = [f(l) for l in L]
        T.sort(reverse=True)
        tmp = sum(T[:M])
        res = max(res, tmp)
    
    print(res)


if __name__ == "__main__":
    main()
