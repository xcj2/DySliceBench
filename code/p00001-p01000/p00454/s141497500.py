# -*- coding: utf-8 -*-
from typing import Union, List
import io, sys
import bisect
from collections import deque


def main():
    w,h = list(map(int, sys.stdin.readline().split()))
    
    if w == h == 0:
        return "END"
    
    n = int( sys.stdin.readline() )
    x1y1x2y2_list = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

    X1,Y1,X2,Y2 = list(map(list, zip(*x1y1x2y2_list)))

    all_X = compress(X1,X2,w)
    all_Y = compress(Y1,Y2,h)

    matrix =[ [0]*len(all_X) for _ in range(len(all_Y)) ]
    

    for i in range(n):
        matrix[ Y1[i] ][ X1[i] ] += 1
        matrix[ Y2[i] ][ X2[i] ] += 1
        matrix[ Y2[i] ][ X1[i] ] -= 1
        matrix[ Y1[i] ][ X2[i] ] -= 1


    for row in range(len(matrix)):
        for col in range(1, len(matrix[0])):
            matrix[row][col] += matrix[row][col-1]
    
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] += matrix[row-1][col]

    del matrix[-1]

    for row in range(len(matrix)):
        del matrix[row][-1]

    
    cnt = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                cnt += 1
                bfs_paint(matrix, col, row, cnt)


    print(cnt)


def compress(A1 :list, A2 :list, max_A):
    all_A = []
    #delta = [-1, 0, 1]
    delta = [0]

    for a in (A1 + A2):
        for d in delta:
            val = a + d

            if 0 <= val <= max_A:
                all_A.append(a + d)

    all_A += [0, max_A]
    all_A = sorted(set(all_A))

    for i in range(len(A1)):
        A1[i] = bisect.bisect_left(all_A, A1[i])
        A2[i] = bisect.bisect_left(all_A, A2[i])
    
    return all_A


def bfs_paint(matrix :List[list], col :int, row :int, cnt :int):
    queue = deque([ (col, row) ])
    matrix[row][col] = cnt
    delta = [(0,1),(0,-1),(1,0),(-1,0)]  # (column, row)

    while queue:
        c,r = queue.popleft()

        for d in delta:
            next_c = c + d[0]
            next_r = r + d[1]

            if (0 <= next_c < len(matrix[0])) and (0 <= next_r < len(matrix)) and \
                matrix[next_r][next_c] == 0:

                matrix[next_r][next_c] = cnt
                queue.append( (next_c, next_r) )


if __name__ == "__main__":
    while True:
        ret = main()
        
        if ret == "END":
            break

