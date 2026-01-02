import heapq
import itertools
inf = 10 * 18

H, W = map(int, input().split())
map = [input() for _ in range(H)]
heuristic = {(i, j): int(((H - i) ** 2 + (W - j) ** 2) ** 0.5) for j in range(W) for i in range(H)}
count_white = sum([s.count(".") for s in map])

def astar(init_pos, goal):
    passed_list = [init_pos]
    init_score = distance(passed_list) + heuristic.setdefault(init_pos, inf)
    checked = {init_pos: init_score}
    searching_heap = []
    heapq.heappush(searching_heap, (init_score, passed_list))
    while len(searching_heap) > 0:

        score, passed_list = heapq.heappop(searching_heap)
        last_passed_pos = passed_list[-1]
        if last_passed_pos == goal:
            return passed_list
        for pos in nexts(last_passed_pos):
            new_passed_list = passed_list + [pos]
            pos_score = distance(new_passed_list) +  heuristic.setdefault(pos, inf)
            if pos in checked and checked[pos] <= pos_score:
                continue

            checked[pos] = pos_score
            heapq.heappush(searching_heap, (pos_score, new_passed_list))

    return []

def distance(path):
    return len(path)

def nexts(pos):
    i = pos[0]
    j = pos[1]
    res = []
    
    for p in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
        if 0<=p[0]<=H-1 and 0<=p[1]<=W-1 and map[p[0]][p[1]] != "#":
            res.append(p)

    return res
    
path = astar((0,0), (H-1,W-1))

if len(path) == 0:
    print(-1)
else:
    print(count_white - len(path))