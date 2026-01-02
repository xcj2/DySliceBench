import sys
H, W = [int(i) for i in input().split(" ")]
board = [["0" for w in range(W+2)] for h in range(H+2)]

for h in range(H):
    tmp = list(input())
    for w in range(W):
        board[h+1][w+1] = tmp[w]

def printBoard():
    for h in range(H+2):
        for w in range(W+2):
            sys.stdout.write(board[h][w])
            sys.stdout.write(" ")
        sys.stdout.write("\n")

def check(h,w):
    if board[h][w-1] == "#":
        return True
    if board[h][w+1] == "#":
        return True
    if board[h-1][w] == "#":
        return True
    if board[h+1][w] == "#":
        return True
    return False

def solve():
    flag = True
    for h in range(1, H+1):
        for w in range(1, W+1):
            if board[h][w] == "#":
                flag = check(h, w)
            else:
                pass
            if not flag:
                return flag
    return flag

if solve():
    print("Yes")
else:
    print("No")
