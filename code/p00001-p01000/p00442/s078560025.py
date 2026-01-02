# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0519

"""
import sys
from sys import stdin
from collections import deque
input = stdin.readline


def bfs(s):
    global Colors
    global Output
    global In_degrees
    global Is_unique

    q = deque()
    q.append(s)
    Colors[s] = GRAY

    while q:
        u = q.popleft()
        Output.append(u)

        pending = []
        for e in Out_edges[u]:
            In_degrees[e] -= 1
            if In_degrees[e] == 0 and Colors[e] == WHITE:
                Colors[e] = GRAY
                pending.append(e)
        if len(pending) > 1:
            Is_unique = False
        for e in pending:
            q.append(e)


def topologial_sort(n):
    global Colors
    global In_degrees
    global Is_unique

    for u in range(1, n+1):
        if In_degrees[u] == 0 and Colors[u] == WHITE:
            if In_degrees.count(0) > 1:
                Is_unique = False
            bfs(u)


BLACK, GRAY, WHITE = 0, 1, 2
Colors = []
Output = []
In_degrees = []
Out_edges = []
Is_unique = True

def main(args):
    global Out_edges
    global Colors
    global In_degrees
    global Is_unique

    n = int(input())            #  ???????????°
    m = int(input())            #  ???????????±?????°
    Out_edges = [[] for _ in range(n+1)]
    In_degrees = [0] * (n + 1)
    In_degrees[0] = -1
    Colors = [WHITE] * (n + 1)

    scores = [[int(x) for x in input().split()] for _ in range(m)]

    for w, l in scores:
        In_degrees[l] += 1
        Out_edges[w].append(l)

    topologial_sort(n)

    for d in Output:
        print(d)
    if Is_unique:
        print(0)
    else:
        print(1)



if __name__ == '__main__':
    main(sys.argv[1:])
    