# coding: utf-8
import sys
import itertools


def sr(): return sys.stdin.readline().rstrip()


def ir(): return int(sr())


def lr(): return list(map(int, sr().split()))


S = sr()
SIZE = len(S)
ans = 0


def dfs(depth, p_list):
    global ans

    if depth == SIZE - 1:
        sum_list = []
        T = S
        for j, p in enumerate(p_list):
            if p:
                sum_list.append(int(S[SIZE - len(T): j + 1]))
                T = S[j + 1:]
        if T:
            sum_list.append(int(T))
        # print(p_list, sum_list, T)
        ans += sum(sum_list)

        return

    for i in range(2):
        p_list[depth] = i
        dfs(depth + 1, p_list)


def main():

    p_list = [0] * (SIZE - 1)
    dfs(0, p_list)

    print(ans)


main()
