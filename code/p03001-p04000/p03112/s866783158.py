#!/usr/bin/env python3
import sys
from bisect import bisect_left

def solve(A: int, B: int, Q: int, s: "List[int]", t: "List[int]", x: "List[int]"):
    for qi in range(Q):
        start = x[qi]
        nearest_s = bisect_left(s,start)
        nearest_t = bisect_left(t,start)

        left_s = s[nearest_s-1] if nearest_s != 0 else -10**12
        right_s = s[nearest_s] if nearest_s != A else 10**12
        left_t = t[nearest_t-1] if nearest_t != 0 else -10**12
        right_t = t[nearest_t] if nearest_t != B else 10**12
                
        leftleftdist = start - min(left_s,left_t) 
        rightrightdist = max(right_s,right_t)-start 
        leftrightdist = min(start-left_s+right_t-left_s, start-left_t+right_s-left_t)
        rightleftdist = min(right_t-start+right_t-left_s, right_s-start+right_s-left_t)
        answer = min(leftleftdist,rightrightdist,rightleftdist,leftrightdist)
    
        print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    t = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(A, B, Q, s, t, x)

if __name__ == '__main__':
    main()
