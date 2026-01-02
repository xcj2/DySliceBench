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
    
N, = getIntList()
#print(N)

zd = {}

for i in range(2, N+1):
    for j in range(2,N+1):
        while i%j==0:
            if j not in zd:
                zd[j] = 0
            zd[j]+=1
            i = i//j
z1 = []
for x in zd:
    if zd[x]>=2:
        z1.append(zd[x])
dprint(z1)
re = 0
def search(ki, zt, ti):
    if ti>=len(zt):
        global re
        re+=1
        return
    global z1
    if ki >= len(z1):
        return
    search(ki+1, zt,ti)
    if z1[ki] +1 >= zt[ti]:
        search(ki+1, zt,ti+1)

search(0, [75,], 0)
search(0, [3,25], 0)
search(0, [25,3], 0)
search(0, [15,5], 0)
search(0, [5,15], 0)
search(0, [3,5, 5], 0)
search(0, [5,3, 5], 0)
search(0, [5,5, 3], 0)


print(re)


