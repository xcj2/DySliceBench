import copy

h, w, k = map(int, input().split())
grid = []
for _ in range(h):
    curRow = list(input())
    grid.append(curRow)

def countBlack(g):
    result = 0
    for row in g:
        result += row.count("#")
    return result

choices = list(range(h)) + list(range(w))


def checkChoice(path):
    curGrid = copy.deepcopy(grid)
    for i in range(h):
        if path[i]:
            for j in range(w):
                curGrid[i][j] = "r"
    for j in range(h, len(choices)):
        if path[j]:
            curCol = j - h
            for i in range(h):
                curGrid[i][curCol] = "r"
    return countBlack(curGrid) == k

result = 0
def solve(i, path):
    global result
    if i == len(choices):
        result += checkChoice(path)
    else:
        path.append(True)
        solve(i + 1, path)
        path.pop()
        path.append(False)
        solve(i + 1, path)
        path.pop()

solve(0, [])
print(result)