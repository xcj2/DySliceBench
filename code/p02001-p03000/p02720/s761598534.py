import collections, math

local = False
if local:
    file = open("inputt.txt", "r")

def inp():
    if local:
        return file.readline().rstrip()
    else:
        return input().rstrip()

def ints():
    return [int(_) for _ in inp().split()]



K = int(inp())

nex = [[0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9],[8,9]]
globcount = 0

def dfs(curdepth, curval):
    if curdepth<0:
        return False
    
    if curdepth==0:
        global globcount
        globcount += 1

        if globcount==K:
            print(curval)
            return True

    nexarr = nex[int(curval[-1])]
    for j in range(len(nexarr)):
        if dfs(curdepth-1, curval+str(nexarr[j])):
            return True
    
    return False


for depth in range(1, 15):
    found = False
    for i in range(1, 10):
        if dfs(depth-1, str(i)):
            found = True
            break
    
    if found:
        break