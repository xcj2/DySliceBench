#!/usr/bin/env python3
import sys
from collections import defaultdict


def sim(N, s, t, d, i):
    # print(s, i)
    curr = i
    for tt, dd in zip(t, d):
        if tt == s[curr]:
            if dd == "R":
                curr += 1
                # print("cuz", tt, dd, curr)
            else:
                curr -= 1
                # print("cuz", tt, dd, curr)
        if curr >= N:
            return "right"
        elif curr < 0:
            return "left"
    return "stay"


# def dfs_2(N, Q, s, t, d):
#     # 消滅は、(s[-1],R)の呪文
#     if Q == 0:
#         return 0
#     ans = 0
#     for i in range(Q):
#         if t[i] == s[-1] and d[i] == 'R':
#             ans += 1 + dfs_2(N, i, s[:-1], t[:i], d[:i])
#     return ans


def solve(N: int, Q: int, s: str, t: "List[str]", d: "List[str]"):

    wa = 0

    ca, cb = -1, N
    while True:
        if ca == cb or ca + 1 == cb:
            break
        # 右側に飛び出す
        curr = (cb+ca) // 2
        # print("1 ca, curr, cb", ca, curr, cb)
        state = sim(N, s, t, d, curr)
        if state == "right":
            cb = curr
        else:
            ca = curr

    # print("1 ca, curr, cb", ca, curr, cb)
    wa += N - cb

    ca, cb = -1, N
    while True:
        if ca == cb or ca + 1 == cb:
            break
        # 左に飛び出す
        curr = (cb+ca) // 2
        # print("2 ca, curr, cb", ca, curr, cb)
        state = sim(N, s, t, d, curr)
        # print("2 ", state)
        if state == "left":
            ca = curr
        else:
            cb = curr
    # print("2 ca, curr, cb", ca, curr, cb)
    wa += ca+1

    print(N-wa)
    # print(sim(N, s, t, d, 1))
    # guide = defaultdict(list)
    # for i in range(N):          # O(N)
    #     guide[s[i]] += [i]
    # pos = [1]*N

    # for i in range(Q):          # O(Q*(N/26))
    #     direc = 1 if d[i] == 'R' else -1
    #     copied = guide[t[i]].copy()
    #     guide[t[i]] = []
    #     for j in copied:
    #         pos[j] -= 1
    #         if 0 <= j + direc and j + direc < N:
    #             pos[j+direc] += 1
    #             guide[s[j+direc]] += [j+direc]
    #             # print("here", s[j+direc])
    #     # print(pos)
    #     # print(guide)
    # print(sum(pos))
    # return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    s = next(tokens)  # type: str
    t = [str()] * (Q)  # type: "List[str]"
    d = [str()] * (Q)  # type: "List[str]"
    for i in range(Q):
        t[i] = next(tokens)
        d[i] = next(tokens)
    solve(N, Q, s, t, d)


if __name__ == '__main__':
    main()
