from sys import stdin
from collections import deque

def read_graph(v, e):
    A = [ [float('inf')]*v for _ in range(v) ]
    for i in range(v):
        A[i][i] = 0
    for _ in range(e):
        line = list(stdin.readline().strip().split())
        i = line[0]
        j = line[1]
        k = line[2]
        A[int(i)][int(j)] = int(k)
    return A

def worshall_floyd(A, v):
    for k in range(v):
        for i in range(v):
            if A[i][k] == float('inf'):
                continue
            for j in range(v):
                if A[k][j] == float('inf'):
                    continue
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    return A

def print_ans(A, v):
    NEGATIVE = False
    for i in range(v):
        if A[i][i] < 0:
            NEGATIVE = True
    if NEGATIVE:
        print('NEGATIVE CYCLE')
    else:
        for i in A:
            print(*[str(k).upper() for k in i], sep=' ')

v, e = [int(i) for i in input().split()]
A = read_graph(v, e)
A = worshall_floyd(A, v)
print_ans(A, v)

