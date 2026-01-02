import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    d = dict()
    for i in range(1, n + 1):
        d[i] = input_int_list()[::-1]
    day = 0
    candi = set(range(1, n + 1))
    rest = (n * (n - 1)) // 2
    while rest:
        played = set()
        for a in candi:
            if d[a] and d[d[a][-1]][-1] and a == d[d[a][-1]][-1]:
                played.add(a)
                played.add(d[a][-1])

        if not played:
            break

        candi.clear()

        rest -= len(played) // 2
        for a in played:
            candi.add(a)
            d[a].pop()
            # if d[a]:
            #     candi.add(d[a][-1])
        day += 1

    if rest == 0:
        print(day)
    else:
        print(-1)


if __name__ == "__main__":
    main()
