import sys
# sys.setrecursionlimit(100000)
from collections import Counter


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input()
    S_cnt = Counter(S).most_common()

    def simulation(org, target):
        cnt = 0
        while org.count(target) != len(org):
            t = ""
            for i in range(len(org) - 1):
                if org[i] == target or org[i + 1] == target:
                    t += target
                else:
                    t += org[i]
            cnt += 1
            org = t
        return cnt
    ans = float("inf")
    for k, v in S_cnt:
        ans = min(simulation(S, k), ans)
    print(ans)

    return


if __name__ == "__main__":
    main()
