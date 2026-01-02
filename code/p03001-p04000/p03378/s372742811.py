import sys
import math
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))

def main():
    n,m,x = i2()
    a = intl()
    c1,c2 = 0,0
    for i in range(x,n+1):
        #print(i)
        if i in a:
            c1 += 1
    for i in range(0,x+1):
        #print(i)
        if i in a:
            c2 += 1
    print(min(c1,c2))
if __name__ == "__main__":
    main()