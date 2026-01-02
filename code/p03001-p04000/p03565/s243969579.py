import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    t = S()
    ans = "UNRESTORABLE"
    for i in range(len(s)-len(t),-1,-1):
        part = s[i:i+len(t)]
        for schar, tchar in zip(part, t):
            if schar!=tchar and schar!="?":
                break
        else:
            ans = s[:i] + t + s[i+len(t):]
            ans = ans.replace("?","a")
            break
    print(ans)
main()
