import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
## libs ##
from collections import deque
#======================================================#
def main():
    n = II()
    aa = [II() for _ in range(n)]
    aa.sort()
    maxv = 0
    if n%2==0:
        sumv = 0
        l = aa[:n//2]
        r = aa[n//2:]
        sumv += sum(2*ri for ri in r)
        sumv -= r[0]
        sumv -= sum(2*li for li in l)
        sumv += l[-1]
        maxv = max(maxv, sumv)
    else:
        sumv = 0
        l = aa[:n//2]
        r = aa[n//2:]
        sumv += sum(2*ri for ri in r)
        sumv -= r[0]+r[1]
        sumv -= sum(2*li for li in l)
        maxv = max(maxv, sumv)

        sumv = 0
        l = aa[:n//2+1]
        r = aa[n//2+1:]
        sumv += sum(2*ri for ri in r)
        sumv -= sum(2*li for li in l)
        sumv += l[-1]+l[-2]
        maxv = max(maxv, sumv)
    print(maxv)

if __name__ == '__main__':
    main()