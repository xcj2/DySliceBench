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
        line = list(S())
        board.append(["."] + line + ["."])
    board.append(["." for _ in range(w+2)])
    table = [[False]*(w+2) for _ in range(h+2)]
    exp = [[1,0],[0,1],[-1,0],[0,-1]]

    for i in range(h+2):
        for j in range(w+2):
            if board[i][j] == ".":
                table[i][j] = True
            else:
                for x,y in exp:
                    if board[i+x][j+y] == "#":
                        table[i][j] = True
    from functools import reduce
    def kakeru(lst):
        return reduce(lambda x,y: x and y,lst)
    ans = True
    for line in table:
        ans &= kakeru(line)
    print("Yes" if ans else "No")
main()                  
