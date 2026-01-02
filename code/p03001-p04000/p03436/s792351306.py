import sys
#input = sys.stdin.readline
from itertools import chain

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
initial = sum(row.count("#") for row in grid)
dire = [(1,0),(0,1),(-1,0),(0,-1)]

def out(y, x):
    return y < 0 or y >= H or x < 0 or x >= W

def wall(y, x):
    return grid[y][x] == "#"

def can_go(y, x, explored):
    return not (out(y, x) or wall(y, x) or (y, x) in explored)

def succs(explored):
    def succs_(point):
        y = point[0]
        x = point[1]
        return [(y+h, x+w) for h, w in dire if can_go(y+h, x+w, explored)]
    return succs_

def bfs(frontier, explored, count):
    if not frontier:
        return -1
    elif any(map(lambda point: point == (H-1, W-1), frontier)):
        return count
    else:
        frontier_ = set(chain(*map(succs(explored), frontier)))
        return bfs(frontier_, explored | frontier_, count+1)
    
def main():
    path_count = bfs([(0, 0)], set([(0, 0)]), 1)
    if path_count == -1:
        print(-1)
    else:
        print(H*W - path_count - initial)

main()