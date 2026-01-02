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
zp = []
for i in range(1, 31):
    zp.append(2**i)

dprint(zp)
    
N, = getIntList()
#print(N)

za = getIntList()

tc = collections.Counter(za)
za.sort(reverse = True)

r = 0
for x in za:
    if tc[x]==0: continue
    tc[x] -= 1
    for y in zp:
        if y<= x: continue
        g = y - x
        if g> x:
            break
        if tc[g] >0:
            r +=1
            tc[g] -=1
print(r)            
        





