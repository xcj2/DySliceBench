import numpy as np
import heapq


def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def main():
    s = input()
    K = ii()

    sub = []
    for i in range(len(s)):
        sub.append(s[i:])

    heapq.heapify(sub)
    minsub = heapq.heappop(sub)

    if len(minsub) >= K:
        print(minsub[:K])
        return

    cand = []
    for i in range(1, len(minsub)+1):
        cand.append(minsub[:i])
    K -= len(minsub)
    assert K > 0

    while K > 0:
        minsub_ = heapq.heappop(sub)
        for i in range(1, len(minsub_)+1):
            if not minsub_[:i] in cand:
                cand.append(minsub_[:i])
                K -= 1
                if K == 0:
                    print(minsub_[:i])
                    return

if __name__ == '__main__':
    main()