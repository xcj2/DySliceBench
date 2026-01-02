#!/usr/bin/env python
# coding: utf-8

import queue

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class BFS:
    def __init__(self, h, w, board):
        self.h = h
        self.w = w
        self.board = board
        self.num_empty = 0
        for x in range(1, w+1):
            for y in range(1, h+1):
                if self.board[y][x] == '.':
                    self.num_empty += 1
        self.cost = [[-1 for _ in range(w+2)] for _ in range(h+2)]

    def search(self):
        q = queue.Queue()
        q.put((1, 1))
        self.cost[1][1] = 1
        while not q.empty():
            p = q.get()
            x, y = p[0], p[1]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if self.board[ny][nx] == '#':
                    continue
                if self.cost[ny][nx] >= 0:
                    continue
                q.put((nx, ny))
                self.cost[ny][nx] = self.cost[y][x]+1
        c = self.cost[self.h][self.w]
        if c == -1:
            return -1
        else:
            return self.num_empty - c

def main():
    h, w = rli()
    board = []
    board.append('#'*(w+2))
    for _ in range(h):
        board.append('#'+input()+'#')
    board.append('#'*(w+2))
    bfs = BFS(h, w, board)
    ans = bfs.search()
    print(ans)



if __name__ == '__main__':
    main()
