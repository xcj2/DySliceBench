#!/usr/bin/env python3
import sys
import queue

def solve(N: int, Q: int, a: "List[int]", b: "List[int]", p: "List[int]", x: "List[int]"):
    # initialize count
    count = [0] * N
    for j in range(Q):
        count[p[j]-1] += x[j]
    # initialize tree vertice adjacency list
    adj_list = [ [] for i in range(N) ]
    for i in range(N-1):
        u, v = a[i] - 1, b[i] - 1
        adj_list[u] += [v]
        adj_list[v] += [u]
    # BFS from root, which is 0-th node
    explored = [False] * N
    myqueue = queue.Queue()
    explored[0] = True
    myqueue.put(0)
    while(not myqueue.empty()):
        u = myqueue.get()
        for v in adj_list[u]:
            if explored[v] == False:
                myqueue.put(v)
                explored[v] = True
                count[v] += count[u]
    print(' '.join([str(i) for i in count]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]" 
    x = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        p[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, Q, a, b, p, x)

if __name__ == '__main__':
    main()
