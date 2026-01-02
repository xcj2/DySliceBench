def BFS_one_search(map_,counts,y,x,wall):
    can_be_new_count = []
    new_ques = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i * j == 0 and i != j:
                if counts[y + i][x + j] != -1:
                    can_be_new_count.append(counts[y + i][x + j] + 1)
                elif not(map_[y + i][x + j] in wall):
                    new_ques.append((y + i,x + j))
    new_count = min(can_be_new_count) if len(can_be_new_count) > 0 else 0
    return new_count,new_ques

def breadth_first_search(map_,s_y,s_x,wall = ['#']):
    ques = [(s_y,s_x)]
    counts = []
    for _ in range(len(map_)):
        counts.append([-1] * len(map_[0]))
    while(len(ques) > 0):
        here_count,new_que = BFS_one_search(map_,counts,ques[0][0],ques[0][1],wall)
        counts[ques[0][0]][ques[0][1]] = here_count
        for i in range(len(new_que)):
            if not new_que[i] in ques:
                ques.append(new_que[i])
        ques.pop(0)
    return counts

def make_map_data(H,W,wall = '#',make_wall = True):
    map_ = []
    if make_wall:
        map_.append([wall] * (W + 2))
        for _ in range(H):
            map_.append([wall] + list(input()) + [wall])
        map_.append([wall] * (W + 2))
    else:
        for _ in range(H):
            map_.append(list(input()))
    return map_
H,W= (int(i) for i in input().split())  
s_y = 1
s_x = 1
g_y = H 
g_x = W
map_ = make_map_data(H,W,make_wall = True)
min_counts = breadth_first_search(map_,s_y,s_x)[g_y][g_x]
if min_counts == -1:
    print(-1)
else:
    wall_count = 0
    for y in range(H + 2):
        for x in range(W + 2):
            if map_[y][x] == '#':
                wall_count += 1
    #print(min_counts)
    print((H + 2) * (W + 2) - wall_count - (min_counts + 1))