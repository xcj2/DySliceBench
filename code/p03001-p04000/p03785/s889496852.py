import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,c,k = LI()
    ans = 0
    cnt = 0
    period = -1
    dps = [None for _ in range(n)]
    for i in range(n):
        dps[i] = I()
    dps.sort()
    
    for dp in dps:        
        if cnt == c or dp > period:
            ans += 1
            cnt = 1
            period = dp+k
        else:
            cnt += 1

    print(ans)
main()            
