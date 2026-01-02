import sys
import math
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":pass
a ,b =i2()
n = int(a//0.08)
m = int(b//0.1)
for i in range(n+1,2*n):
    for j in range(m+1,2*m):
        if i == j and math.floor(i*0.08) == a  and b == math.floor(j*0.1):
            print(i)
            exit()
print(-1)