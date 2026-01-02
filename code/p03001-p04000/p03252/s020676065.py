#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str, T: str):
    n = len(S)
    m_in = {}
    m_out = {}
    for i in range(n):
        if (S[i] in m_in and m_in[S[i]] != T[i]) or (T[i] in m_out and m_out[T[i]] != S[i]):
            ret = NO
            print(ret)
            return
        else:
            m_in[S[i]] = T[i]
            m_out[T[i]] = S[i]
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)

if __name__ == '__main__':
    main()
