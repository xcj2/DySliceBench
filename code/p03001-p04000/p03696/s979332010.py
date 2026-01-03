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
    S = input()
    stack = []
    for s in S:
        if not stack:
            stack.append(s)
        elif s == "(":
            stack.append(s)
        elif s == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
    cnt = defaultdict(int)
    for s in stack:
        cnt[s] += 1
    left = cnt[")"]
    right = cnt["("]
    ans = ("(" * left) + S + (")" * right)
    print(ans)

    return


if __name__ == "__main__":
    main()
