# import sys
# input = sys.stdin.readline
# import re
import math
import itertools

def main():
    h, w, k = input_list()
    maze = []
    for H in range(h):
        maze.append(list(input()))

    ans = []
    a = 0
    all = 0
    for l in maze:
        a += l.count('#')
        all += l.count('#')
    ans.append(a)
    hash_list_H = []
    kumi = 0
    for H in range(h):
        if maze[H].count('#') == k:
            kumi += 1
        # hash_list_H.append(maze[H].count('#'))

    hash_list_W = []
    for W in range(w):
        a = 0
        for H in range(h):
            if maze[H][W] == '#':
                a += 1
        if a == k:
            kumi += 1
        hash_list_W.append(a)
    # kumi = hash_list_W.count(k) + hash_list_H.count(k)
    # if all == k:
    #     kumi += 1
    # for H in range(1, h+1):
    #     for c in itertools.combinations(hash_list_H, H):
    #         if all - sum(list(c)) == k:
    #             kumi += 1
    # for W in range(1, w+1):
    #     for c in itertools.combinations(hash_list_W, W):
    #         if all - sum(list(c)) == k:
    #             kumi += 1
    # print(kumi)
    ss = 0
    # for H in range(1, h+1):
    #     for W in range(1, w+1):
    #         for hc in itertools.combinations(hash_list_H, H):
    #             for wc in itertools.combinations(hash_list_W, W):
    #                 if all - (sum(hc) + sum(wc)) == k:
    #                     ss += 1
    # print(kumi+ss)
    r = 0
    done = []
    for H in range(h+1):
        for W in range(w+1):
            for hc in itertools.combinations(range(h), H):
                for wc in itertools.combinations(range(w), W):
                    if (hc, wc) in done:
                        continue
                    done.append((hc, wc))
                    if count(maze, hc, wc) == k:
                        r += 1
    print(r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def count(mazes, hc, wc):
    hc = list(hc)
    wc = list(wc)
    r = 0
    for hi, row in enumerate(mazes):
        if hi in hc:
            continue
        for wi, m in enumerate(row):
            if wi in wc:
                continue
            if m == '#':
                r += 1
    return r

def input_list():
    return list(map(int, input().split()))

def input_list_str():
    return list(map(str, input().split()))

if __name__ == '__main__':
    main()

