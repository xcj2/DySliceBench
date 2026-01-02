def bfs(field,H,W,start_x,start_y,tmp_N):
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    que = []
    que.append([start_x,start_y])
    INF = 1000000
    min_path = [[INF] * W for i in range(H)]
    min_path[start_y][start_x] = 0
    while len(que) != 0:
        current = que.pop(0)
        for d in direction:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            if 0 <= nx < W and 0 <= ny < H and field[ny][nx] != "X" and min_path[ny][nx] == INF:
                min_path[ny][nx] = min_path[current[1]][current[0]] + 1
                if field[ny][nx] == tmp_N:
                    return nx,ny,min_path[ny][nx]
                else:
                    que.append([nx,ny])

def getField():
    matrix = []
    first = input().strip()
    H,W,N = map(int,first.split())
    for i in range(H):
        row = list(input().strip())
        for j in range(W):
            if row[j].isdigit():
                row[j] = int(row[j])
        matrix.append(row)
    return matrix,H,W,N

def getStart(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == "S":
                return x,y

def main():
    matrix,H,W,N = getField()
    sx,sy = getStart(matrix)
    distance = 0
    tmp_x,tmp_y,tmp_dist = bfs(matrix,H,W,sx,sy,1)
    distance += tmp_dist
    tmps = [tmp_x,tmp_y]
    for k in range(N-1):
        tmp_x,tmp_y,tmp_dist = bfs(matrix,H,W,tmps[0],tmps[1],k+2)
        distance += tmp_dist
        tmps = [tmp_x,tmp_y]
    print(distance)

if __name__=='__main__':
    main()