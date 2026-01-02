import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    s = S()
    right, left = 0, 0
    ans = n
    for i in s:
        right += 1 if i=="E" else 0

    for i, char in enumerate(s):
        right -= 1 if char=="E" else 0
        cnt = left + right
        ans = min(ans,cnt)
        left += 1 if char=="W" else 0

    print(ans)
main()
