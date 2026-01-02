#!/usr/bin/env python3
import sys
INF = float("inf")


def Run_length_encoding(S: str):
    """AAABBC -> [(A, 3), (B, 2), (C, 1)]
    """
    ans = []
    curr = S[0]
    counter = 0
    for c in S:
        if c == curr:
            counter += 1
        else:
            ans.append((curr, counter))
            curr = c
            counter = 1
    ans.append((curr, counter))
    return ans


def solve(S: str, K: int):

    rle = Run_length_encoding(S)
    fchr, fcnt = rle[0]
    lchr, lcnt = rle[-1]
    if len(rle) == 1:
        print(fcnt*K//2)
        return

    ans = 0
    for c, cnt in rle:
        ans += cnt//2
    ans *= K

    if K > 1 and fchr == lchr:
        ans -= K*(fcnt//2)
        ans -= K*(lcnt//2)
        ans += (K-1)*((fcnt+lcnt)//2)
        ans += fcnt//2
        ans += lcnt//2

    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)


if __name__ == '__main__':
    main()
