
def getStart(field):
    search_field = field[1:]
    for y in range(len(search_field)):
        for x in range(len(search_field[0])):
            if search_field[y][x] == "S":
                return x,y+1


def bfs(field,start_x,start_y,goal_N):
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    gotten_cheese = 1
    distance = 0
    que = []
    que.append([start_x,start_y,gotten_cheese,distance])
    INF = 1
    min_path = [[INF for j in range(field[0][1])] for i in range(field[0][0])]
    while len(que) != 0:
        current = que.pop(0)
        for d in direction:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            if 0 <= nx < field[0][1] and 1 <= ny < field[0][0]+1 and field[ny][nx] != "X" and min_path[ny-1][nx] == INF:
                if field[ny][nx] == current[2]:
                    if field[ny][nx] == goal_N:
                        print(current[3]+1)
                        return
                    else:
                        que = []
                        que.append([nx,ny,current[2]+1,current[3]+1])
                        min_path = [[INF for j in range(field[0][1])] for i in range(field[0][0])]
                        break
                else:
                    que.append([nx,ny,current[2],current[3]+1])
                    min_path[ny-1][nx] = 0


def main(field):
    sx,sy = getStart(field)
    bfs(field,sx,sy,field[0][2])

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