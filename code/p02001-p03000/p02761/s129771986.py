#!/usr/bin/env python3
import sys

def solve(N: int, M: int, s: "List[int]", c: "List[int]"):

    dict = {}
    ans = "1"
    if N == 1:
        ans = "0"
    for i in range(N-1):
        ans += "0"

    for i in range(len(s)):
        if s[i] == 1 and c[i] == 0 and N != 1:
            print(-1)
            return
        # dup check
        if s[i] in dict.keys():
            if dict[s[i]] != c[i]:
                print(-1)
                return
        else:
            dict[s[i]] = c[i]

        ans = ans[:s[i]-1] + str(c[i]) + ans[s[i]:]
    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, s, c)

if __name__ == '__main__':
    main()
