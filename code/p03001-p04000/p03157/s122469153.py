h,w = list(map(int, input().split())) 
s=list([]) 
foot = list([False for i in range(w)] for j in range(h))

def is_new_white(i,j):
    global h,w, s, foot
    if ((i<0) or (j<0) or (i>=h) or(j>=w)):
        return False
    elif (not foot[i][j] and (s[i][j] == ".")):
        return True
    else:
        return False

def is_new_black(i,j):
    global h,w, s, foot
    if ((i<0) or (j<0) or (i>=h) or(j>=w)):
        return False
    elif (not foot[i][j] and (s[i][j] == "#")):
        return True
    else:
        return False

def check(i,j):
    global s, foot
    black = list([])
    white = list([])
    white_c = 0
    black_c = 0
    
    if foot[i][j] == True:
        return 0
    else:
        if s[i][j] == "#":
            black.append([i,j])
            foot[i][j] = True
            black_c += 1
        else:
            white.append([i,j])
            foot[i][j] = True
            white_c += 1

    while (bool(black) or bool(white)):
        while bool(black):
            pos = black.pop(0)
            tmp = [[pos[0]-1,pos[1]],[pos[0],pos[1]-1],[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]
            for x in tmp:
                if is_new_white(x[0], x[1]):
                    white_c += 1
                    white.append([x[0],x[1]])
                    foot[x[0]][x[1]] = True

        while bool(white):
            pos = white.pop(0)
            tmp = [[pos[0]-1,pos[1]],[pos[0],pos[1]-1],[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]
            for x in tmp:
                if is_new_black(x[0], x[1]):
                    black_c += 1
                    black.append([x[0],x[1]])
                    foot[x[0]][x[1]] = True
    return black_c * white_c


for i in range(h):
    s.append(input())

ans = 0
for i in range(h):
    for j in range(w):
        ans += check(i,j)

print(ans)