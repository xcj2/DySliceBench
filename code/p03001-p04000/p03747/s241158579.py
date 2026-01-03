# coding: utf-8
import array, bisect, collections, heapq, itertools, math, random, re, string, sys, time
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
 
 
def II(): return int(input())
def ILI(): return list(map(int, input().split()))
def IAI(LINE): return [ILI() for __ in range(LINE)]
def IDI(): return {key: value for key, value in ILI()}
 
 
def solve(N, L, T, pos, dir):
    # 円形だからどんなにぶつかっても1-Nまで順番に並んでいることは変わりない。
    pos_mov = []
    for i in range(1, N + 1):
        if dir[i] == 1:
            pos_mov.append((pos[i] + T) % L)
        elif dir[i] == 2:
            pos_mov.append((pos[i] - T) % L)

    pos_mov.sort()

    count = 0

    for i in range(2, N + 1):
        dif = pos[i] - pos[1]
        if dir[1] == 1:
            if dir[i] == 2:
                if dif <= 2 * T:
                    count += ((2 * T - dif) // L + 1)
        elif dir[1] == 2:
            if dir[i] == 1:
                if (L - dif) <= 2 * T:
                    count += ((2 * T - (L - dif))// L + 1)

    if dir[1] == 1:
        pos1 = (pos[1] + T) % L
        num1 = count % N + 1
    elif dir[1] == 2:
        pos1 = (pos[1] - T) % L
        num1 = -count % N + 1

    if dir[1] == 1:
        ind = max([i for i in range(1, N + 1) if pos_mov[i - 1] == pos1])
    else:
        ind = min([i for i in range(1, N + 1) if pos_mov[i - 1] == pos1])

    ans = []
    for i in range(1, N + 1):
        ans.append(pos_mov[(ind - num1 + i) % N - 1])

    return ans


def main():
    N, L, T = ILI()
    pos = dict()
    dir = dict()
    for i in range(1, N + 1):
        X, W = ILI()
        pos[i] = X
        dir[i] = W

    ans = solve(N, L, T, pos, dir)
    for i in ans:
        print(i)


if __name__ == "__main__":
    main()
