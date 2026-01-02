import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    key = "keyence"
    ans = False
    if s == key:
        ans = True
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            ex = s[:i] + s[j:]
            if ex == key:
                ans = True
    print("YES" if ans else "NO")
main()            
