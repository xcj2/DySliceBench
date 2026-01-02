def read_valus():
    return map(int, input().split())


def read_list():
    return list(read_valus())


def read_lists(N):
    return [read_list() for n in range(N)]


def f(T, n):
    N = len(T)
    b = format(n, "015b")[::-1][:N]
    
    for n, s in enumerate(b):
        if s == "1":
            for x, y in T[n]:
                if int(b[x]) != y:
                    return False
    return True


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
    for n in range(2 ** N - 1, -1, -1):
        bit_count = bin(n).count("1")
        if res >= bit_count:
            continue

        if f(T, n):
            res = max(res, bit_count)  

    print(res)


if __name__ == "__main__":
    main()
