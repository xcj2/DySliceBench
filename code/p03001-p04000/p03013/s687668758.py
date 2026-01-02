#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, M: int, a: "List[int]"):
    i = 2
    arr = [1, 1]
    seek = 0
    while seek < len(a) and a[seek]==1:
        arr[1] = 0
        seek+=1
    while i<=N:
        if seek < len(a) and i == a[seek]:
            arr[0], arr[1] = arr[1], 0
            seek+=1
        else:
            arr[0], arr[1] = arr[1], (arr[0]+arr[1])%MOD
        i+=1
    print(arr[1])

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
