import sys
import math
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [str(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))
def f(n):
    #print(l)
    if n%2 == 0:
        return n//2
    else:
        return 3*n + 1
if __name__ == "__main__":
    n = i()
    c = 0
    cnt = 1
    l = [n]
    #if n != 2 or n != 1 or n != 4:l = [n]
    while c < 2:
        n = f(n)
        cnt += 1
        if n in l:
            print(cnt)
            break
        l.append(n)