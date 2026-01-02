h,w = map(int, input().split())
maze = [input() for i in range(h)]
route = [[0] * w for i in range(h)]
white = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            white += 1
 
 
class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item_1, item_2):
        self.stack.append([item_1,item_2])
    def pop(self):
        result = self.stack.pop(0)
        return result[0],result[1]
 
 
def min_route():
    global h,w
    stack = MyStack()
    stack.push(1,1)
    route[0][0] = 0
    n = 0
    while len(stack.stack) >= 1:
        y,x = stack.pop()
        route_num = route[y-1][x-1] + 1
        if y != h:
            if maze[y][x-1] == '.' and route[y][x-1] == 0:
                stack.push(y+1,x)
                route[y][x-1] += route_num
        if y != 1:
            if maze[y-2][x-1] == '.' and route[y-2][x-1] == 0:
                stack.push(y-1,x)
                route[y-2][x-1] += route_num
        if x != w:
            if maze[y-1][x] == '.' and route[y-1][x] == 0:
                stack.push(y,x+1)
                route[y-1][x] += route_num
        if x != 1:
            if maze[y-1][x-2] == '.' and route[y-1][x-2] == 0:
                stack.push(y,x-1)
                route[y-1][x-2] += route_num
        if route[h-1][w-1]  != 0:
            return route[h-1][w-1]
        n += 1
    print(-1)
    exit()
 
ans = white - min_route() - 1
 
if ans < 0:
    print(-1)
else:
    print(ans)