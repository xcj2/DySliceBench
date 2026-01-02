#!/usr/bin/env python3
import sys
import collections

def solve(N: int, a: "List[int]"):
    counter = collections.Counter(a)
    aset = set(a)
    answer = 0
    for aa in aset:
        answer += (counter[aa]-aa) if counter[aa]>=aa else counter[aa]
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
