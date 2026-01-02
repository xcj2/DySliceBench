#!/usr/bin/env python3
# Traveling
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    t.insert(0, 0)
    x.insert(0, 0)
    y.insert(0, 0)
    print(trabelable(N, t, x, y))

def trabelable(N, t, x, y):
    for i in range(N):
        delta_t = t[i+1] - t[i]
        dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
        if delta_t < dist:
            return NO
        if delta_t % 2 != dist % 2:
            return NO
    return YES

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]" 
    x = [int()] * (N)  # type: "List[int]" 
    y = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, t, x, y)

if __name__ == '__main__':
    main()
