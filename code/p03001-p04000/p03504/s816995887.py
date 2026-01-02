#!/usr/bin/env python3
import sys


def solve(N: int, C: int, s: "List[int]", t: "List[int]", c: "List[int]"):
    imos = [[0]*(10**5+2) for _ in range(C+1)]
    channel = dict()

    for i in range(N):
        if channel.get(c[i]) != None:
            channel[c[i]].append((s[i],t[i]))
        else:
            channel[c[i]] = [(s[i],t[i])]

    from itertools import accumulate
    for c in range(1,C+1):
        if channel.get(c) == None:
            continue
        ## start 時間でsort
        channel[c].sort(key = lambda x:x[0])

        # 終了時間が現在一番遅いものを保持しておく
        t_last = -1
        for s,t in channel[c]:
            if t_last == s:
                imos[c][t_last+1] +=1
            else:
                imos[c][s] += 1
            t_last = t
            imos[c][t+1] -= 1
        imos[c]=list(accumulate(imos[c]))

    answer = 0
    for i in range(1,10**5+1):
        a = 0
        for c in range(1,C+1):
            a += imos[c][i]
        answer = max(a,answer)
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    s = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, s, t, c)

if __name__ == '__main__':
    main()
