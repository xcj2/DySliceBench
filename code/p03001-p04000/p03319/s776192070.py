import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,k = LI()
    a = LI()
    index = a.index(1)
    left = index
    right = n-index-1
    ans = float("inf")

    for i in range(k):
        cl = left-i
        cr = right-(k-i-1)
        if cl < 0 or cr < 0:
            continue
        
        cntl = (cl+k-2)//(k-1) if cl!=0 else 0
        cntr = (cr+k-2)//(k-1) if cr!=0 else 0
        cnt = cntl+cntr+1
        ans = min(ans,cnt)

    print(ans)
    
main()            
