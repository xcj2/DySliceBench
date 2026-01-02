import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = [None] + input_int_list()
    ans = 0
    d = defaultdict(int)
    # i < j とすると、
    # j - i = Ai + Aj
    # Ai + i = j - Aj となる
    # 列の後ろから評価し、条件を満たす個数を足していけば良い
    # 計算量：O(n)
    for i in range(n, 0, -1):
        cur = i + A[i]
        ans += d[cur]
        d[i - A[i]] += 1
    print(ans)

    return


if __name__ == "__main__":
    main()
