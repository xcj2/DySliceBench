#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(a: "List[int]", b: "List[int]"):
    count = [0] * 4
    for i in range(3):
        count[a[i] - 1] += 1
        count[b[i] - 1] += 1
    if max(count) >= 3:
        ret = NO
    else:
        ret = YES
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = [int()] * (3)  # type: "List[int]" 
    b = [int()] * (3)  # type: "List[int]" 
    for i in range(3):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(a, b)

if __name__ == '__main__':
    main()
