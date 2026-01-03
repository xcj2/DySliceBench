import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    from collections import defaultdict
    S = list(input())
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    if (d["N"] == 0 and d["S"] > 0) or (d["N"] > 0 and d["S"] == 0) or (d["W"] == 0 and d["E"] > 0) or (d["W"] > 0 and d["E"] == 0):
        print("No")
    else:
        print("Yes")

    return


if __name__ == "__main__":
    main()
