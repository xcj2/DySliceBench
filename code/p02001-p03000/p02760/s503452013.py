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
a1,a2,a3 = i2()
b1,b2,b3 = i2()
c1,c2,c3 = i2()
l = [a1,a2,a3,b1,b2,b3,c1,c2,c3]
n = i()
for i in range(n):
    k = int(input())
    if k in l:
        try:
            l[l.index(k)] = 0
        except IndexError:pass  
if (l[0] == 0 and l[1] == 0 and  l[2]== 0):
    print("Yes")
elif (l[3] == 0 and l[4] == 0 and  l[5]== 0):
    print("Yes")
elif (l[6] == 0 and l[7] == 0 and  l[8] == 0):
    print("Yes")
elif (l[0] == 0 and l[3] == 0 and  l[6]== 0):
    print("Yes")
elif (l[1] == 0 and l[4] == 0 and  l[7] == 0):
    print("Yes")
elif (l[2] == 0 and l[5] == 0 and  l[8] == 0):
    print("Yes")
elif (l[0] == 0 and l[4] == 0 and  l[8] == 0):
    print("Yes")
elif (l[2] == 0 and l[4] == 0 and l[6] == 0):
    print("Yes")
else:print("No")