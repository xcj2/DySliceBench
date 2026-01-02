_rule = {'N':(1,5,2,3,0,4),'S':(4,0,2,3,5,1),'E':(0,3,1,4,2,5),'W':(0,2,4,1,3,5)}
_idx = {'top':0, 'front':1, 'right':2, 'left':3, 'back':4, 'bottom':5}
_idxmap = ((1,2),(1,1),(2,1),(0,1),(3,1),(1,0))

def motion(dlist, direction):
    templist = dlist
    for i in range(len(direction)):
        templist = [templist[r] for r in _rule[direction[i]]]
    return templist

def stopmotion(dlist, num, distination):
    return dlist.index(num) == _idxmap[distination]
    
def search(dlist, top, front):
    ret = ''
    prepos = _idxmap[dlist.index(top)]
    topxpos, topypos = _idxmap[0]
    xpos = topxpos - prepos[0]
    ypos = topypos - prepos[1]
    if xpos <= 0:
        ret = 'W' * abs(xpos)
    else:
        ret = 'E' * abs(xpos)
    ret += 'N' * abs(ypos)
    
    templist = motion(x, ret)
    
    ret = ''
    prepos = _idxmap[templist.index(front)]
    frontxpos, frontypos = _idxmap[1]
    xpos = frontxpos - prepos[0]
    if xpos <= 0:
        ret = 'W' * abs(xpos)
    else:
        ret = 'E' * abs(xpos)
    return motion(templist, ret)
        
x = input().split()

for _ in range(int(input())):
    top, front = input().split()
    templist = search(x, top, front)
    print(templist[_idx['right']])
