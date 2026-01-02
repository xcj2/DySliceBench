import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    s = S()
    ans = 0
    
    for i in range(1,n):
        left = s[:i]
        right = s[i:]
        leftset = set(left)
        rightset = set(right)
        share = len(leftset & rightset)
        ans = max(ans, share)

    print(ans)
main()