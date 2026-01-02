from sys import stdin


def swqp(ps, li, ri):
    result = ps[:]
    tmp = result[li]
    result[li] = result[ri]
    result[ri] = tmp
    return result


def check(ps):
    for i in range(len(ps) - 1):
        if ps[i] > ps[i + 1]:
            return False
    return True


def main():
    N = int(stdin.readline().rstrip())
    ps = [int(x) for x in stdin.readline().rstrip().split()]
    if check(ps):
        print('YES')
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            if check(swqp(ps, i, j)):
                print('YES')
                return
    print('NO')


if __name__ == "__main__":
    main()
