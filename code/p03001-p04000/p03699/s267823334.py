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
    S = []
    for _ in range(n):
        S.append(input_int())
    ans = sum(S)
    S.sort()
    if ans % 10 != 0:
        print(ans)
        return
    else:
        for s in S:
            if s % 10 != 0:
                print(ans - s)
                return
    print(0)

    return


if __name__ == "__main__":
    main()
