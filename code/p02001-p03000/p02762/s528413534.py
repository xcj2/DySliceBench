#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N, M, K = MI()
    friends = [[] for i in range(N)]
    blocks = [[] for i in range(N)]

    for _ in range(M):
        a, b = MI()
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)

    for _ in range(K):
        a, b = MI()
        a -= 1
        b -= 1
        blocks[a].append(b)
        blocks[b].append(a)

    flag = [-1] * N
    group = 0
    for i in range(N):
        if flag[i] != -1:
            continue
        deque = cl.deque(friends[i])
        flag[i] = group
        while len(deque) > 0:
            target = deque.popleft()
            flag[target] = group
            friends_i = friends[target]
            for frend in friends_i:
                if flag[frend] != -1:
                    continue
                flag[frend] = group
                deque.append(frend)
        group += 1

    groups = [[] for i in range(N)]
    for i in range(len(flag)):
        groups[flag[i]].append(i)
    ans = []
    for i in range(len(groups)):
        groups[i] = set(groups[i])

    for i in range(N):
        i_group = flag[i]
        candidate = len(groups[i_group]) - len(friends[i]) - 1
        for blocking in blocks[i]:
            if blocking in groups[i_group]:
                candidate -= 1
        ans.append(candidate)
    print(" ".join(map(str, ans)))


main()
