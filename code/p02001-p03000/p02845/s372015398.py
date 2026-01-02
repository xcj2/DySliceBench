mod = 1000000007

def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def f(M, a):
    count = M.count(a)
    if count == 0:
        return 0

    for i in range(2, -1, -1):
        if M[i] == a:
            M[i] += 1
            break

    return count


def main():
    N = int(input())
    A = read_list()

    M = [0, 0, 0]
    res = 1

    for a in A:
        res *= f(M, a)
        res %= mod
        if res == 0:
            print(0)
            return

    print(res % mod)


if __name__ == '__main__':
    main()
