import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n,x = I2()
    a = intl()
    a.sort()
    i = 0
    s = 0
    if sum(a) == x:
        print(n)
        exit()
    if sum(a) < x:
        print(n-1)
        exit()
    while s <= x:
        s += a[i]
        i += 1
    print(i-1)