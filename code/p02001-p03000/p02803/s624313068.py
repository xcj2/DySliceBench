
h,w = list(map(int, input().split()))

maze = []
maze.append(['#'] * (w+2))
for i in range(h):
    row = [c for c in input()]
    row.insert(0, '#')
    row.append('#')
    maze.append(row)
maze.append(['#'] * (w+2))

def search(item):
    x, y, dist = item
    ret = [
        (x+i,y+j, dist+1) for (i,j)
        in [(1,0), (-1,0), (0,1), (0,-1)]
        if maze[x+i][y+j] == '.'
    ]
    return ret

def bfs(fn, todo):
    seen = dict()
    for item in todo:
        x, y, d = item
        seen[(x, y)] = True    
    
    longest = 0
    while len(todo) > 0:
        # print("todo", todo)
        # print("seen", seen.keys())
        # print("longest", longest)
        item, todo = todo[0], todo[1:]
        x, y, dist = item
        if dist>longest:
            longest = dist

        for a in fn(item):
            x, y, dist = a
            if (x, y) in seen:
                continue
            seen[(x,y)] = True
            todo.append(a)

    return longest

def calc(x, y):
    return bfs(search, [(x, y, 0)])

longest_longest = 0

for i in range(1, h+1):
    for j in range(1, w+1):
        if maze[i][j] == "#":
            continue
        longest = calc(i, j)

        if longest_longest < longest:
            longest_longest = longest  

print(longest_longest)
