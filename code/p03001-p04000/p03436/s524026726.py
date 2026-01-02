from collections import namedtuple
import pdb

H, W = map(int, input().split())
s = []
visited = []
step = []

Prev = namedtuple('Prev', ('row', 'col', 'num'))
default_black = 0

for _ in range(H):
    line = input()
    for c in line:
        if c=='#':
            default_black += 1
    s.append(line)
    visited.append([0 for _ in range(W)])
    step.append([0 for _ in range(W)])
    

queue = []

step[0][0] = 1

Point = namedtuple('Point', ('row', 'col'))
st = Point(0, 0)
en = Point(H-1, W-1)



def valid(p):
    return (0 <= p.row and p.row < H and 0 <= p.col and p.col < W)

def around_p(p):
    around = [Point(p.row-1, p.col), Point(p.row+1, p.col), Point(p.row, p.col-1), Point(p.row, p.col+1)]
    for a in around:
        yield a

def goal(p):
    return p.row == H-1 and p.col == W-1

def bfs():
    queue = [st]

    while queue:
        cur_p = queue[0]
        queue = queue[1:]
        if goal(cur_p):
            return step[cur_p.row][cur_p.col]
        if visited[cur_p.row][cur_p.col] == 1:
            continue
        cur_step = step[cur_p.row][cur_p.col]
        visited[cur_p.row][cur_p.col] = 1

        for next_p in around_p(cur_p): 
            if not valid(next_p):
                continue
            if s[next_p.row][next_p.col] == '#':
                continue
            if visited[next_p.row][next_p.col] == 1:
                continue
            queue.append(next_p)
            step[next_p.row][next_p.col] = cur_step + 1
                        
    return -1

def main():
    ans = bfs()
    if ans == -1:
        print(ans)
    else:
        print(H*W - default_black - ans)


main()
    
