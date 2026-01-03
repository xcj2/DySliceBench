#!/usr/bin/env python3
import sys

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = sorted(list(set(table)))
    return table
def keta(i):
    return len(str(i))

def solve(N: int):
    yakusuu = divisor(N)
    answer = 11
    LEN = len(yakusuu)
    for i in range(LEN):
        answer = min(answer,max(keta(yakusuu[i]),keta(yakusuu[LEN-1-i])))
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
