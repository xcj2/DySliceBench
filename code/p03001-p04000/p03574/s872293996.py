import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    h,w = LI()
    board = [["." for _ in range(w+2)]]
    for _ in range(h):
        s = S()
        s = list(s)
        s = ["."] + s + ["."]
        board.append(s)
    board.append(["." for _ in range(w+2)])

    exp = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for y in range(1,h+1):
        for x in range(1,w+1):
            if board[y][x] == ".":
                cnt = 0
                for u,r in exp:
                    if board[y-u][x-r] == "#":
                        cnt += 1
                board[y][x] = str(cnt)

    for line in board[1:-1]:
        line = "".join(line[1:-1])
        print(line)
main()