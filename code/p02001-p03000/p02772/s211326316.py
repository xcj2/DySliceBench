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
a = intl()
cnt1 = 0
cnt2 = 0
for i in range(n):
    if a[i]%2 == 0:
        cnt1 += 1
        if a[i]%3 == 0 or a[i]%5 == 0:
            cnt2 += 1
print("APPROVED" if cnt1 == cnt2 else "DENIED")