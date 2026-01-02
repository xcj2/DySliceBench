#!/usr/bin/env python3
import sys
import itertools
INF = float("inf")


def solve(N: int, s: "List[str]"):

    ABcount = 0
    Aend = 0
    Bstart = 0
    AendBstart = 0
    for i in range(N):
        ABcount += s[i].count("AB")
        if s[i][0] == "B" and s[i][-1] == "A":
            AendBstart += 1
        elif s[i][0] == "B":
            Bstart += 1
        elif s[i][-1] == "A":
            Aend += 1

    if AendBstart == 0:
        ABcount += min(Aend, Bstart)
    else:
        if Aend + Bstart > 0:
            ABcount += min(Aend, Bstart) + AendBstart
        else:
            ABcount += AendBstart - 1
    print(ABcount)
    # if AendBstart > 1:
    #     ABcount += AendBstart - 1
    #     AendBstart = 1
    # if Aend > 0 or Bstart > 0:
    #     ABcount += min(Aend, Bstart)+AendBstart
    # print(ABcount)

    # 愚直
    # print("愚直")
    # ans = []
    # for kumi in itertools.permutations(s, N):
    #     ans.append("".join(kumi).count("AB"))
    # print(max(ans))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)


if __name__ == '__main__':
    main()
