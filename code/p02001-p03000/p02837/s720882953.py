def read_valus():
    return map(int, input().split())


def read_list():
    return list(read_valus())


def read_lists(N):
    return [read_list() for n in range(N)]


def get_bit(n, i):
    return n >> i & 1


def f(T, n):
    # for i in range(len(T)):
    #     if get_bit(n, i):
    #         for x, y in T[i]:
    #             if get_bit(n, x) != y:
    #                 return False
    # return True
    return all(all(get_bit(n, x) == y for x, y in T[i]) for i in range(len(T)) if get_bit(n, i))


def main():
    N = int(input())
    T = [[] for n in range(N)]
    for n in range(N):
        A = int(input())
        for _ in range(A):
            x, y = read_valus()
            x -= 1
            T[n].append((x, y))

    res = 0
    for n in range(2 ** N):
        if f(T, n):
            res = max(res, bin(n).count("1"))

    print(res)


if __name__ == "__main__":
    main()
