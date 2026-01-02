def count(state: int, ss: list):
    res = 0
    for s in ss:
        res += ((state >> s) & 1)
    return res


assert count(0b011, [0, 1]) == 2
assert count(0b011, [2]) == 0


def is_on(state: int, p: int, ss: list):
    return count(state, ss) % 2 == p


def main():
    N, M = map(int, input().split())

    sss = [
        list(map(lambda x: int(x)-1, input().split()))[1:] for _ in range(M)
    ]

    ps = list(map(int, input().split()))

    cnt = 0
    for state in range(0, 2**N):
        cnt += all(map(lambda x: is_on(state, x[0], x[1]), zip(ps, sss)))
    print(cnt)


if __name__ == '__main__':
    main()