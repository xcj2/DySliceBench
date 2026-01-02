import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()

ans = 0
b_start,a_end,b_start_a_end = 0,0,0
for i in range(N):
    s = S()
    if s[0] == 'B' and s[-1] == 'A':
        b_start_a_end += 1
    elif s[0] == 'B':
        b_start += 1
    elif s[-1] == 'A':
        a_end += 1
    for j in range(len(s)-1):
        if s[j] == 'A' and s[j+1] == 'B':
            ans += 1

if b_start_a_end == 0:
    print(ans+min(b_start,a_end))
else:
    ans += b_start_a_end-1
    if a_end > 0:
        ans += 1
        a_end -= 1
    if b_start > 0:
        ans += 1
        b_start -= 1
    ans += min(b_start,a_end)
    print(ans)
