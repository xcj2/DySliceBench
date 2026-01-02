# ref: https://qiita.com/masashi127/items/0c794e28f4b295ad82c6
import heapq
import itertools


def astar(init_pos, goal,dg):
    passed_list = [init_pos]
    init_score = distance(passed_list) + heuristic(init_pos,goal)
    checked = {init_pos: init_score}
    searching_heap = []
    heapq.heappush(searching_heap, (init_score, passed_list))
    while len(searching_heap) > 0:
        score, passed_list = heapq.heappop(searching_heap)
        last_passed_pos = passed_list[-1]
        if last_passed_pos == goal:
            return passed_list
        for pos in nexts(dg,last_passed_pos):
            new_passed_list = passed_list + [pos]
            pos_score = distance(new_passed_list) + heuristic(pos,goal)
            if pos in checked and checked[pos] <= pos_score:
                continue
            checked[pos] = pos_score
            heapq.heappush(searching_heap, (pos_score, new_passed_list))
    return []

def solve_dungeon(dungeon):
    init = find_ch(dungeon,"S")
    goal = find_ch(dungeon,"G")
    path = astar(init, goal,dungeon)

    if len(path) > 0:
        return True
    else:
        return False

def find_ch(dg,ch):
    for i, l in enumerate(dg):
        for j, c in enumerate(l):
            if c == ch:
                return (i, j)

def nexts(dg,pos):
    wall = "x"
    for a, b in [[' + 1',''], [' - 1',''], ['',' + 1'], ['',' - 1']]:
        if a or b:
            if dg[eval('pos[0]' + a)][eval('pos[1]' + b)] != wall:
                yield (eval('pos[0]' + a), eval('pos[1]' + b))

def heuristic(pos,goal):
    return ((pos[0] - goal[0]) ** 2 + (pos[1] - goal[1]) ** 2) ** 0.5

def distance(path):
    return len(path)

def render_path(dg,path):
    buf = [[ch for ch in l] for l in dg]

    for pos in path[1:-1]:
        buf[pos[0]][pos[1]] = "*"

    buf[path[0][0]][path[0][1]] = "s"
    buf[path[-1][0]][path[-1][1]] = "g"
    return ["".join(l) for l in buf]

if __name__ == "__main__":
    while(True):
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
        xs,ys = map(int,input().split())
        xg,yg = map(int,input().split())
        n = int(input())
        d = [ list(map(int,input().split())) for _ in range(n)]
        m = [[0]*w for _ in range(h)]
        for e in d:
            for r in m[e[3]-1:e[3]+2*(e[1]+1)-1]:
                r[e[2]-1:e[2]+2*(2-e[1])-1] = [e[0]]*2*(2-e[1])
        ans = False
        for col in range(1,6):
            txt = [''.join(str(' ' if e==col else 'x') for e in f)  for f in m]
            if txt[ys-1][xs-1] == "x" or txt[yg-1][xg-1] == "x":
                continue
            txt[ys-1] = txt[ys-1][:xs-1] + 'S' + txt[ys-1][xs:]
            txt[yg-1] = txt[yg-1][:xg-1] + 'G' + txt[yg-1][xg:]
            for i in range(len(txt)):
                txt[i] = 'x' + txt[i] + 'x'
            txt.insert(0,'x'*(w+2))
            txt.append('x'*(w+2))
            ans |= solve_dungeon(txt)
            if ans:
                print("OK")
                break
        if not ans: print("NG")


