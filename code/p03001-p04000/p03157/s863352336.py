#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args,  file=sys.stderr)
    dprint('debug mode')
except Exception:
    def dprint(*args, **kwargs):
        pass



inId = 0
outId = 0
if inId>0:
    dprint('use input', inId)
    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #标准输出重定向至文件
if outId>0:
    dprint('use output', outId)
    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #标准输出重定向至文件
    atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit
    
H, W = getIntList()
#print(N)
zs = []
dprint(H,W)
for i in range(H):
    s = input()
    zs.append(s)
    dprint(s)
zu = [  [(i,j) for j in range(W) ]  for i in range(H) ]
dprint(11111)
def getr(p):
    #dprint('?', p)
    if p == zu[ p[0] ] [p[1] ]:
        return p
    np = getr(zu[ p[0] ] [p[1] ])
    zu[ p[0] ] [ p[1] ] = np
    return np
dprint(11111)
def uuu( p0, p1) :
    p0 = getr(p0)
    p1 = getr(p1)
    #dprint(p0, p1)
    zu[ p0[0] ] [p0[1] ] =  p1
dprint(zu)
dprint(zs)
for i in range(H):
    for j in range(W): 
        if i>0:
            if zs[i-1][j] != zs[i][j]:
                uuu( (i-1,j), (i,j) )
        if j>0:
            if zs[i][j-1] != zs[i][j]:
                uuu( (i,j-1), (i,j) )
         
dprint(11111) 
zr = dict()
dprint(11111)
for i in range(H):
    for j in range(W):
        p = (i,j)
        p = getr(p)
        if p not in zr:
            zr[p] = [0,0]
        if zs[i][j] == '.':
            zr[p][0] +=1
        else:
            zr[p][1] +=1
dprint(zr)            
r = 0
for x in zr:
    r += zr[x][0] * zr[x][1]
    
print(r)
