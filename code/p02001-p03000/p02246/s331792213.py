import heapq

distance = (
            (0,1,2,3,1,2,3,4,2,3,4,5,3,4,5,6),
            (1,0,1,2,2,1,2,3,3,2,3,4,4,3,4,5),
            (2,1,0,1,3,2,1,2,4,3,2,3,5,4,3,4),
            (3,2,1,0,4,3,2,1,5,4,3,2,6,5,4,3),
            (1,2,3,4,0,1,2,3,1,2,3,4,2,3,4,5),
            (2,1,2,3,1,0,1,2,2,1,2,3,3,2,3,4),
            (3,2,1,2,2,1,0,1,3,2,1,2,4,3,2,3),
            (4,3,2,1,3,2,1,0,4,3,2,1,5,4,3,2),
            (2,3,4,5,1,2,3,4,0,1,2,3,1,2,3,4),
            (3,2,3,4,2,1,2,3,1,0,1,2,2,1,2,3),
            (4,3,2,3,3,2,1,2,2,1,0,1,3,2,1,2),
            (5,4,3,2,4,3,2,1,3,2,1,0,4,3,2,1),
            (3,4,5,6,2,3,4,5,1,2,3,4,0,1,2,3),
            (4,3,4,5,3,2,3,4,2,1,2,3,1,0,1,2),
            (5,4,3,4,4,3,2,3,3,2,1,2,2,1,0,1),
            (6,5,4,3,5,4,3,2,4,3,2,1,3,2,1,0),
           )

def d_manhattan(node_list):
    s = 0
    for i in range(16):
        j = node_list[i] - 1
        if j == -1: continue
        s += distance[i][j]
    return s

def moveNode(node_list, space, direction):
    node_tmp = node_list[:]
    node_tmp[space], node_tmp[space + direction] = node_tmp[space + direction], node_tmp[space]
    return node_tmp

class board:
    def __init__(self, node_list, move):
        self.node = node_list
        self.space = node_list.index(0)
        self.move = move
        self.h = d_manhattan(node_list)
        self.f = self.move + self.h

    def makeBoard(self, node_close):
        node_now = self.node
        space = self.space
        move = self.move
        x_s = space%4
        y_s = space//4
        if x_s < 3:
            node_tmp = moveNode(node_now, space, 1)
            if tuple(node_tmp) not in node_close:
                yield board(node_tmp, move + 1)
        if x_s > 0:
            node_tmp = moveNode(node_now, space, -1)
            if tuple(node_tmp) not in node_close:
                yield board(node_tmp, move + 1)
        if y_s < 3:
            node_tmp = moveNode(node_now, space, 4)
            if tuple(node_tmp) not in node_close:
                yield board(node_tmp, move + 1)
        if y_s > 0:
            node_tmp = moveNode(node_now, space, -4)
            if tuple(node_tmp) not in node_close:
                yield board(node_tmp, move + 1)

b_open = []
n_close =set()
n_goal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
n_start = []

for i in range(4):
    inp = list(map(int, input().split()))
    n_start.extend(inp)

b_start = board(n_start, 0)
heapq.heappush(b_open, (b_start.f, b_start.h, 0, b_start))

i = 0
while b_open:
    _, _, _, b_now = heapq.heappop(b_open)
    if b_now.node == n_goal:
        b_goal = b_now
        break
    n_close.add(tuple(b_now.node))
    for b_new in b_now.makeBoard(n_close):
        heapq.heappush(b_open, (b_new.f, b_new.h, i, b_new))
        i += 1

print(b_goal.move)