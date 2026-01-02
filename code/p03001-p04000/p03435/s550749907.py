import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    grid = []
    for _ in range(3):
        grid.append(LI())
    
    ans = True
    l1 = grid[0][1] - grid[0][0]
    l2 = grid[0][2] - grid[0][1]
    ans &= grid[1][1] - grid[1][0] == l1 and grid[1][2] - grid[1][1] == l2
    ans &= grid[2][1] - grid[2][0] == l1 and grid[2][2] - grid[2][1] == l2

    r1 = grid[1][0] - grid[0][0]
    r2 = grid[1][0] - grid[0][0]
    ans &= grid[1][1] - grid[0][1] == r1 and grid[1][1] - grid[0][1] == r2
    ans &= grid[1][2] - grid[0][2] == r1 and grid[1][2] - grid[0][2] == r2
    print("Yes" if ans else "No")
main()            
