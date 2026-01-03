import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

n = I()
t = Intl()
m = I()
px = [Intl() for i in range(m)]
#print(px)
s = sum(t)
time = s
for i in range(m):
    print(time-t[px[i][0]-1]+px[i][1])
    time = s