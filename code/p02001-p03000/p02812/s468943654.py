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

n = i()
s = s()
cnt = 0
l = s.split("ABC")
if len(l) == 1:
    print(0)
else:
    print(len(l)-1)