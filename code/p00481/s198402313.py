
def getStart(field):
    search_field = field[1:]     # cut the first [H,W,N] for min_path matrix
    for y in range(len(search_field)):
        for x in range(len(search_field[0])):
            if search_field[y][x] == "S":
                return x,y+1


def bfs(field,start_x,start_y,goal_N):
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    gotten_cheese = 1
    distance = 0
    que = []
    que.append([start_x,start_y])
    INF = 1000000
    min_path = [[INF] * field[0][1] for i in range(field[0][0])]
    min_path[start_y-1][start_x] = 0
    while len(que) != 0:
        current = que.pop(0)
        for d in direction:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            if 0 <= nx < field[0][1] and 1 <= ny < field[0][0]+1 and field[ny][nx] != "X" and min_path[ny-1][nx] == INF:
                min_path[ny-1][nx] = min_path[current[1]-1][current[0]] + 1
                if field[ny][nx] == gotten_cheese: # at the same cheese-power number
                    distance += min_path[ny-1][nx]
                    if field[ny][nx] == goal_N: # goal
                        print(distance)
                        return
                    else: # not goal, but could eat cheese
                        que = []
                        que.append([nx,ny])
                        gotten_cheese += 1
                        min_path = [[INF] * field[0][1] for i in range(field[0][0])]
                        min_path[ny-1][nx] = 0
                        break
                else:
                    que.append([nx,ny])


def main(field):
    sx,sy = getStart(field)
    bfs(field,sx,sy,field[0][2])

# field = [[10,10,9],
# [".","X",".",".",".","X",".","S",".","X"],
# [6,".",".",5,"X",".",".","X",1,"X"],
# [".",".",".","X","X","X","X",".",".","X"],
# ["X",".",".",9,"X",".",".",".","X","."],
# [8,".","X",2,"X",".",".","X",3,"X"],
# [".",".",".","X","X",".","X",4,".","."],
# ["X","X",".",".",".",".",7,"X",".","."],
# ["X",".",".","X",".",".","X","X",".","."],
# ["X",".",".",".","X",".","X","X",".","."],
# [".",".","X",".",".",".",".",".",".","."]]
#
# main(field)

matrix = []
while True:
    row = input().rstrip().split()
    if len(row) == 3:
        re_row = []
        for i in row:
            re_row.append(int(i))
        matrix.append(re_row)
    else:
        re_row = []
        for char in row[0]:
            if char.isdigit():
                re_row.append(int(char))
            else:
                re_row.append(char)
        matrix.append(re_row)
    if len(matrix) == int(matrix[0][0]) + 1:
        main(matrix)
        break