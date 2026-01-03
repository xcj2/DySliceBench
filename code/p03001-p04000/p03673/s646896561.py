#!/usr/bin/env python3
import sys
from collections import deque

def solve(n: int, a: "List[int]"):
    ## 左右左と追加していく
    li = deque()

    for i in range(n):
        if i%2==0:
            li.appendleft(a[i])
        else:
            li.append(a[i])
    
    if n%2 == 0:
        li = list(li)[::-1]
    
    
    print(" ".join(map(str,list(li))))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
