import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,k = LI()
    r,s,p = LI()
    t = list(S())
    ans = 0

    for i in t[:k]:
        if i=="r":
            ans += p
        elif i == "s":
            ans += r
        elif i == "p":
            ans += s
    
    for i in range(k,n):
        if t[i]=="r":
            if t[i-k]=="r":
                t[i] = ""
            else:
                ans += p
        elif t[i]=="s":
            if t[i-k]=="s":
                t[i] = ""
            else:
                ans += r
        elif t[i]=="p":
            if t[i-k]=="p":
                t[i] = ""
            else:
                ans += s
        
    print(ans)
main()            
