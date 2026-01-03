W,H,N = (int(i) for i in input().split())
fill_map = [[ 0 for i in range(H)] for j in range(W)]
def count(fill_map):
    counter = 0
    for i in range(W):
        for j in range(H):
            if fill_map[i][j] == 0:
                counter += 1
    return counter

def _fill(l1,l2,fill_map):
    for i in range(l1[0],l2[0]+1):
        for j in range(l1[1],l2[1]+1):
            fill_map[i][j] = 1
            
def fill(axis,direction,fill_map):
    if axis == 0:
        if direction == 0:
            #fill left side
            _fill([0,0],[x-1,H-1],fill_map)
        else:
            #fill right side
            _fill([x,0],[W-1,H-1],fill_map)
    else:
        if direction == 0:
            #fill down side
            _fill([0,0],[W-1,y-1],fill_map)
        else:
            #fill upper side
            _fill([0,y],[W-1,H-1],fill_map)



for i in range(N):
    x,y,a = (int(i) for i in input().split())
    if a == 1:
        fill(0,0,fill_map)
    elif a == 2:
        fill(0,1,fill_map)
    elif a == 3:
        fill(1,0,fill_map)
    elif a == 4:
        fill(1,1,fill_map)

result = count(fill_map)
print(result)

