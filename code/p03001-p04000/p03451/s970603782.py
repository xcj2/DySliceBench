# coding: UTF-8
n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
tile = [a1, a2]
x, y = 0, 0
score = 0

def move(i, x, y):
    score = tile[y][x]
    for j in range(i):
        x, y = right(x, y)
        score += tile[y][x]
    x, y = under(x, y)
    score += tile[y][x]
    for j in range(n-i-1):
        x, y = right(x, y)
        score += tile[y][x]
    return(score)

def right(x, y):
    if(x < n-1):
        return(x+1, y)
    else:
        return(x, y)

def under(x, y):
    if(y < 1):
        return(x, y+1)
    else:
        return(x, y)

for i in range(n):
    now_score = move(i, 0, 0)
    if(score < now_score):
        score = move(i, 0, 0)

print(score)