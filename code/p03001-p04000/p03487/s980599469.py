#!/usr/bin/env python3
import sys
from collections import Counter

def solve(N: int, a: "List[int]"):
    counter = Counter(a)
    answer = 0
    for key,value in counter.items():
        if key >value:
            answer += value
        else:
            answer += value-key
    print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
