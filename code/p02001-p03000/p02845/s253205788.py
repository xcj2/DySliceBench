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
    A = input_int_list()
    MOD = 10**9 + 7
    cnt = 1
    x, y, z = 0, 0, 0
    for a in A:
        tmp = 0
        is_used = False  # x,y,zのどこかに配った。
        if a == x:
            tmp += 1
            if not is_used:
                x += 1
                is_used = True
        if a == y:
            tmp += 1
            if not is_used:
                y += 1
                is_used = True
        if a == z:
            tmp += 1
            if not is_used:
                z += 1
                is_used = True
        cnt *= tmp
        cnt = cnt % MOD
    print(cnt)

    return


if __name__ == "__main__":
    main()
