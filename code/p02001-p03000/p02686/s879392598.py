#!/usr/bin/env python3

import sys, heapq
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, S: "List[str]"):
    tmp = []
    for i in range(N):
        cur = 0
        mn = 0
        for c in S[i]:
            if c == '(':
                cur += 1
            else:
                cur -= 1
                mn = min(mn, cur)
        tmp.append((mn, cur))

    tmp.sort(key=lambda x: (x[1] < 0, (-x[0] if x[1] >= 0 else -(x[1] - x[0]))))
    #tmp.sort(key=lambda x: (x[1] < 0, -x[0], x[1]))
    #print(tmp)

    cur = 0
    for mn, cnt in tmp:
        #print(cur, mn, cnt)
        if abs(mn) > cur:
            print(NO)
            return
        cur += cnt

    if cur == 0:
        ret = YES
    else:
        ret = NO
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
