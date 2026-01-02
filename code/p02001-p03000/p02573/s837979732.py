#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N, M = MI()
    relations = [set([]) for i in range(N)]
    for i in range(M):
        a, b = MI()
        a -= 1
        b -= 1
        relations[a].add(b)
        relations[b].add(a)

    grouped = [-1] * N
    group_num = [0] * N

    group = -1

    for i in range(len(grouped)):
        if grouped[i] != -1:
            continue
        deque = cl.deque(relations[i])
        group += 1

        while len(deque) > 0:
            target = deque.popleft()
            friends = relations[target]
            for friend in friends:
                if grouped[friend] != -1:
                    continue
                grouped[friend] = group
                group_num[group] += 1
                deque.append(friend)

    ans = max(group_num)
    print(max(ans, 1))


main()
