import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    n, h= LI()
    huri = [0 for _ in range(n)]
    nage = [0 for _ in range(n)]
    use = []
    
    for i in range(n):
        huri[i], nage[i] = LI()

    mx = max(huri)

    for katana in nage:
        if katana >= mx:
            use.append(katana)

    use.sort(reverse=True)
    ans = 0
    for used in use:
        h -= used
        ans += 1
        if h<=0:
            break

    if h>0:
        ans += (h+mx-1)//mx

    print(ans)



main()
