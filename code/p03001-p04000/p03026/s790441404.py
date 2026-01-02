#!/usr/bin/env python3
import sys
#from queue import Queue


def solve(N: int, a: "List[int]", b: "List[int]", C: "List[int]"):
    conn = [[] for _ in range(N)]
    for i in range(N - 1):
        conn[a[i] - 1].append(b[i] - 1)
        conn[b[i] - 1].append(a[i] - 1)
    #counts = [Queue() for _ in range(N)]
    counts = [[] for _ in range(N)]
    for i in range(N):
        l = len(conn[i])
        #counts[l].put([i, conn[i]])
        counts[i] = [len(conn[i]), conn[i], 0, i]
    #counts.sort(key=lambda x: x[0])

    ret = 0
    #print(counts)
    C.sort()
    idx = 0
    while idx < N:
        for cnt in counts:
            if cnt[2] == 0 and cnt[0] <= 1:
                cnt[2] = C[idx]
                idx += 1
                for node in cnt[1]:
                    counts[node][0] -= 1
            ##ret += C[i] * cnt[0]
    vals = [0] * N
    for cnt in counts:
        vals[cnt[3]] = cnt[2]
    for i in range(N - 1):
        ret += min(vals[a[i] - 1], vals[b[i] - 1])
    print(ret)
    print(' '.join([str(v) for v in vals]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a, b, c)

if __name__ == '__main__':
    main()
