import sys

def setLine(tempH, line):
    for i in range(0, len(line)):
        geo[tempH][i] = line[i:i+1]

def solve():
    person = 0
    for i in range(0,H):
        for j in range(0,W):
            if geo[i][j] is not "_":
                search(i,j)
                person += 1
    print(person)

def search(i,j):
    temp = geo[i][j]
    geo[i][j] = "_"
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    for a in range(0,4):
        idx = i + dx[a]
        jdy = j + dy[a]
        if(isOnMap(idx, jdy)):
            if(isNeededToSolve(temp, idx, jdy)):
                search(idx,jdy)

def isOnMap(i,j):
    return (0<=i and 0<=j and i<H and j<W)

def isNeededToSolve(temp,i,j):
    target = geo[i][j]
    return (target is not "_" and temp is target)

limit = 10**7
sys.setrecursionlimit(limit)

H = -1
W = -1
tempH = 0
geo = [[0 for i in range(1)]for j in range(1)]
repeat = True
while repeat:
    line = input()
    if H is -1 and W is -1:
        H = int(line.split(" ")[0])
        W = int(line.split(" ")[1])
        geo = [[0 for i in range(W)] for j in range(H)]
    else:
        setLine(tempH, line)
        tempH+=1

    #break
    if H is 0 and W is 0:
        break

    #solve
    if tempH is H:
        solve()
        H = -1
        W = -1
        tempH = 0