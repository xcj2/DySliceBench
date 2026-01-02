#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    ret = YES
    t = [0] + t
    x = [0] + x
    y = [0] + y
    for i in range(1, N + 1):
        #print(x[i], y[i], t[i])
        dis = abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])
        time = t[i] - t[i - 1]
        if dis > time or dis % 2 != time % 2:
            #print(x[i], y[i], t[i])
            ret = NO
            break
    print(ret)
    return


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
