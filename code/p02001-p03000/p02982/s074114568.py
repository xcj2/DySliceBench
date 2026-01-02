import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

def dist(list1,list2):
    d = 0
    for i in range(len(list1)):
        d += (list1[i]-list2[i])**2
    return math.sqrt(d)
n,d = I2()
x = []
for i in range(n):
    inp = Intl()
    x.append(inp)
#print(x)
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        d = dist(x[i],x[j])
        if int(d) == d:cnt += 1
print(cnt)