import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,a,b,c,d = LI()
    s = "#" + S()
    ans = True
    if a<b and b<c and c<d:
        ans &= "##" not in  s[b:d]
        ans &= "##" not in  s[a:c]
    elif a<b and b<d and d<c:
        ans &= "##" not in  s[b:d]
        ans &= "..." in s[b-1:d+2]
        ans &= "##" not in  s[a:c]
    elif a<c and c<b and b<d:
        ans &= "##" not in  s[b:d]
        ans &= "##" not in  s[a:c]
    
    print("Yes" if ans else "No")
    
main()            
