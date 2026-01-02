import queue
import sys

write = sys.stdout.write

hoge = list(map(int, input().split()))
H = hoge[0]
W = hoge[1]

class Block:
    visited = False
    parent = None
    def __init__(self, c, x, y):
        self.color = c
        self.x = x
        self.y = y

def trace(A, blk):
    blk.color = "r"
    if blk.x == 1 and blk.y == 1:
        return
    trace(A, blk.parent)

def solve(A):
    global H
    global W

    #ゴールとスタートが黒ならむりぽ
    if A[1][1].color == "#" or A[H][W].color == "#":
        return -1

    q = queue.Queue()
    q.put(A[1][1])
    while not q.empty():
        blk = q.get()
        if blk.x == H and blk.y == W: #ゴールに到達したら通ってきた道を戻って関数を抜け出す
            trace(A, blk)
            return 1
        #上:A[blk.x - 1][blk.y]
        #下:A[blk.x + 1][blk.y]
        #右:A[blk.x][blk.y + 1]
        #左:A[blk.x][blk.y - 1]

        #上
        if A[blk.x - 1][blk.y].visited == False and A[blk.x - 1][blk.y].color == ".":
            A[blk.x - 1][blk.y].parent = blk
            A[blk.x - 1][blk.y].visited = True
            q.put(A[blk.x - 1][blk.y])

        #下
        if A[blk.x + 1][blk.y].visited == False and A[blk.x + 1][blk.y].color == ".":
            A[blk.x + 1][blk.y].parent = blk
            A[blk.x + 1][blk.y].visited = True
            q.put(A[blk.x + 1][blk.y])

        #右
        if A[blk.x][blk.y + 1].visited == False and A[blk.x][blk.y + 1].color == ".":
            A[blk.x][blk.y + 1].parent = blk
            A[blk.x][blk.y + 1].visited = True
            q.put(A[blk.x][blk.y + 1])

        #左
        if A[blk.x][blk.y - 1].visited == False and A[blk.x][blk.y - 1].color == ".":
            A[blk.x][blk.y - 1].parent = blk
            A[blk.x][blk.y - 1].visited = True
            q.put(A[blk.x][blk.y - 1])
    return -1



cnt = 0 #ゴール後の白カウント

maze = [[Block("d", i, j) for j in range(W+2)] for i in range(H+2)]
for i in range(1, H+1):
    row = input()
    for j in range(W):
        maze[i][j+1] = Block(row[j], i, j+1)

possible = solve(maze)

if possible == -1:
    print("-1")
else:
    for i in range(1, H+1):
        for j in range(1, W+1):
            if maze[i][j].color == ".":
                cnt += 1
    print(str(cnt))