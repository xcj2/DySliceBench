# https://atcoder.jp/contests/abc162/tasks/abc162_d

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
    S = input()
    r = set()
    g = set()
    b = set()
    for i in range(n):
        if S[i] == "R":
            r.add(i)
        elif S[i] == "G":
            g.add(i)
        else:
            b.add(i)
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s1 = S[i]
            s2 = S[j]
            k = j + (j - i)
            if k > n - 1:
                break
            s3 = S[k]
            if s1 != s2 and s2 != s3 and s3 != s1:
                cnt += 1
    ans = (len(r) * len(g) * len(b)) - cnt
    print(ans)
    return


if __name__ == "__main__":
    main()
