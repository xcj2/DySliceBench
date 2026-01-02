from collections import deque

H, W = map(int, input().split())
S = tuple(map(lambda x:int(x)-1, input().split()))
G = tuple(map(lambda x:int(x)-1, input().split()))
field = []
for _ in range(H):
    field.append(input())

cost = [[-1] * W for _ in range(H)]

def can_go(pos):
    if pos[0] >= 0 and pos[0] < H and pos[1] >= 0 and pos[1] < W:
        if field[pos[0]][pos[1]] == '.' and cost[pos[0]][pos[1]] == -1:
            return True
        else:
            return False
    else:
        return False

def recursive_walk(pos):
    dests = set()
    stack = [pos]
    while stack:
        pos = stack.pop()
        if pos in dests:
            continue
        dests.add(pos)
        stack += walk(pos)
    return dests

def walk(pos):
    dests = []
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_pos = (pos[0]+d[0], pos[1]+d[1])
        if can_go(new_pos):
            dests.append(new_pos)
    return dests

def warp(pos):
    dests = []
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            new_pos = (pos[0]+dy, pos[1]+dx)
            if can_go(new_pos):
                dests.append(new_pos)
    return dests

q = deque()
q.append([S, 0])

while q:
    pos, c = q.popleft()
    if cost[pos[0]][pos[1]] != -1:
        continue
    cost[pos[0]][pos[1]] = c
    if pos == G:
        break
    warp_from = [pos]
    for dest in recursive_walk(pos):
        if cost[dest[0]][dest[1]] == -1:
            cost[dest[0]][dest[1]] = c
            warp_from.append(dest)
    warp_to = set()
    for fr in warp_from:
        for dest in warp(fr):
            if cost[dest[0]][dest[1]] == -1:
                warp_to.add(dest)
    for dest in warp_to:
        q.append((dest, c+1))
print(cost[G[0]][G[1]])


