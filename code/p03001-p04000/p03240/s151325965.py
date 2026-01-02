#!/usr/bin/env python3

def possible_height(cx, cy, infos):
    maxmin = 1
    minmax = 99999999999
    for i in infos:
        hmin, hmax = get_height(cx, cy, *i)
        maxmin = max(maxmin, hmin)
        minmax = min(minmax, hmax)
    if maxmin == minmax:
        return maxmin
    elif maxmin < minmax:  # Undetermined
        raise Exception
    else:  # Impossible
        return None

def get_height(cx, cy, xi, yi, hi):
    hmax = abs(cx - xi) + abs(cy - yi) + hi
    hmin = 1 if hi == 0 else hmax
    return hmin, hmax

def main():
    n = int(input())
    infos = []
    for i in range(n):
        x, y, h = map(int, input().split())
        infos.append((x, y, h))

    for cx in range(101):
        for cy in range(101):
            h = possible_height(cx, cy, infos)
            if h is not None:
                print(cx, cy, h)
                return
    raise Exception

main()
