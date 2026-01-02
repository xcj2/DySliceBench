import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    ans = 0
    if n<10:
        ans = n
    else:
        keta = len(str(n))
        top = int(str(n)[0])
        down = int(str(n)[1:])
        if top == 1:
            if down == 10**(keta-1)-1:
                ans = 1+(keta-1)*9
            else:
                ans = (keta-1)*9
        else:
            if down == 10**(keta-1)-1:
                ans = top+(keta-1)*9
            else:
                ans = top-1+(keta-1)*9
    
    print(ans)

main()            
