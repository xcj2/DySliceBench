import sys

def small(paper, x, y):
    paper[x][y] += 1
    paper[x-1][y] += 1
    paper[x][y-1] += 1
    paper[x][y+1] += 1
    paper[x+1][y] += 1

def medium(paper, x, y):
    small(paper, x, y)
    paper[x-1][y-1] += 1
    paper[x-1][y+1] += 1
    paper[x+1][y-1] += 1
    paper[x+1][y+1] += 1

def large(paper, x, y):
    medium(paper, x, y)
    paper[x-2][y] += 1
    paper[x][y-2] += 1
    paper[x][y+2] += 1
    paper[x+2][y] += 1

def drop(paper, x, y, size):

    if size == 1:
        small(paper, x, y)
    elif size == 2:
        medium(paper, x, y)
    else:
        large(paper, x, y)

    return paper


paper = [[0 for i in range(14)] for j in range(14)]
for s in sys.stdin:
    x, y, size = map(int, s.split(','))
    paper = drop(paper, x+2, y+2, size)

empty = 0
deep = 0

for i in range(10):
    for j in range(10):
        if paper[i+2][j+2] == 0:
            empty += 1
        elif paper[i+2][j+2] > deep:
            deep = paper[i+2][j+2]

print(empty)
print(deep)