#!/usr/bin/env python3
import sys


def solve(N: int, h: "List[int]"):
    print(watering(h))
    return

def watering(h):
    if sum(h) == 0:
        return 0
    else:
        max_height = max(h)
        s, e = max_sub_sequence(h, max_height)
        assert s >= 0 and e < len(h), "invalid s: {} & e: {}".format(s, e)
        if s == 0 and e == len(h)-1:
            return max_height
        elif s == 0:
            diff = max_height - h[e+1]
            h[s:e+1] = [h[e+1]] * (e+1-s)
            return watering(h) + diff
        elif e == len(h)-1:
            diff = max_height - h[s-1]
            h[s:e+1] = [h[s-1]] * (e+1-s)
            return watering(h) + diff
        else:
            if h[s-1] < h[e+1]:
                diff = max_height - h[e+1]
                h[s:e+1] = [h[e+1]] * (e+1-s)
                return watering(h) + diff
            else:
                diff = max_height - h[s-1]
                h[s:e+1] = [h[s-1]] * (e+1-s)
                return watering(h) + diff

def max_sub_sequence(h, max_height):
    i = 0
    j = 0
    while i < len(h):
        if h[i] == max_height:
            j = i + 1
            while j < len(h) and h[j] == max_height:
                j += 1
            j -= 1
            break
        i += 1
    return i, j

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, h)

if __name__ == '__main__':
    main()
