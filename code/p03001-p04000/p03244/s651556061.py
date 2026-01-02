#! /usr/bin/python3
from collections import Counter
import sys

def debug(*f):
    print(*f, file=sys.stderr)

def f(odd, even, N):
    debug(N, odd, even)


def main(N, V):
    debug("N=",N)
    debug("V=",V)
    N = int(N)
    V = [int(x) for x in V.split(" ")]

    odd = Counter(V[0::2]).most_common()
    even = Counter(V[1::2]).most_common()

    if odd[0][0] != even[0][0]: # 異なる文字
        return N - odd[0][1] - even[0][1]
    else:
        if odd[0][1] > even[0][1]:
            return N - odd[0][1] - even[1][1]
        elif odd[0][1] < even[0][1]:
            return N - odd[1][1] - even[0][1]
        elif odd[0][1] == N // 2:
            return N // 2
        else:
            return N - odd[0][1]  - max(odd[1][1], even[1][1])



if 0==1:
    import sys
    assert main("4", "3 1 3 2") == 1
    assert main("4", "1 1 1 1") == 2
    assert main("6", "105 119 105 119 105 119") == 0
    assert main("14", "1 1 1 1 1 1 2 2 2 2 3 4 3 5") == 9

    print("OK", file=sys.stderr)


N = input()
V = input()
print(main(N, V))
