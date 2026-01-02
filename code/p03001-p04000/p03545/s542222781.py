# coding: utf-8
import sys
import itertools


def sr(): return sys.stdin.readline().rstrip()


def ir(): return int(sr())


def lr(): return list(map(int, sr().split()))


S = sr()
ans = 0


def dfs(depth, p_list):
    global ans

    if depth == 4:
        sum_list = []
        T = S
        text = ''
        for j, p in enumerate(p_list):
            if p == 1:
                sum_list.append(int(T[:1]))
            elif p == -1:
                sum_list.append(int(T[:1]) * -1)

            if len(text) == 0:
                text += T[:1]
            else:
                if p == 1:
                    text += '+' + T[:1]
                elif p == -1:
                    text += '-' + T[:1]
            T = T[1:]
        # print(p_list, sum_list)
        ans = sum(sum_list)
        if ans == 7:
            text += '=7'
            print(text)
            exit()

        return

    for i in [1, -1]:
        p_list[depth] = i
        dfs(depth + 1, p_list)


def main():

    p_list = [0] * (4)
    dfs(0, p_list)


main()
