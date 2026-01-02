# coding: utf-8
import sys
import itertools


def sr(): return sys.stdin.readline().rstrip()


def ir(): return int(sr())


def lr(): return list(map(int, sr().split()))


def check(sws):
    on_list = []
    for i in range(M):
        on = 0
        for s in d_dict[i + 1]:
            on += sws[s]
        if on % 2 == p_list[i]:
            on_list.append(True)
        else:
            on_list.append(False)

    return all(on_list)


ans = 0


def dfs(depth, sws):
    global ans

    if depth == 0:
        return check(sws) * 1

    for i in range(2):
        t_sws = sws
        t_sws[depth] = i
        on = dfs(depth - 1, t_sws)
        ans += on

    return 0


N, M = lr()
d_dict = {}
for i in range(M):
    s_list = lr()
    d_dict[i + 1] = s_list[1:]

p_list = lr()

sw_list = [0] * (N + 1)
dfs(N, sw_list)
print(ans)
