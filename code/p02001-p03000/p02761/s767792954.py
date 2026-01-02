import sys
import math
import itertools as it
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":pass
n ,m = i2()
l = [0]*n
for i in range(m):
    s,c = i2()
    if s == 1 and c == 0 and n != 1:
        print(-1)
        exit()
    if l[s-1] == 0 or l[s-1] == c:
        l[s-1] = c
    else:
        print(-1)
        exit()
num = ""
for i in range(n):
    if i == 0 and l[i] == 0 and n != 1:
        num = num + "1"
    else:
        num = num + str(l[i])
num = int(num)
print(num if len(str(num)) == n else -1)