import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ga,sa,ba = map(int, input().split())
gb,sb,bb = map(int, input().split())

def sub1(n, ga, gb):
    return n - (n//ga)*ga + (n//ga)*gb
def sub2(n, ga, gb, sa, sb):
    ans = -1
    for i in range((n//sa)+1):
        val = sub1(n - (i*sa), ga, gb) + (i*sb)
        ans = max(ans, val)
    return ans
def sub3(n, ga, gb, sa, sb, ba, bb):
    ans = -1
    for i in range((n//ba)+1):
        val = sub2(n - (i*ba), ga, gb, sa, sb) + (i*bb)
        ans = max(ans, val)
    return ans

arg1 = []
arg2 = []
for a,b in [(ga,gb), (sa,sb), (ba,bb)]:
    if a<b:
        arg1.extend([a,b])
    elif a>b:
        arg2.extend([b,a])
d = {
    0: lambda n: n,
    1: sub1,
    2: sub2,
    3: sub3
}
nn = d[len(arg1)//2](n, *arg1)
nnn = d[len(arg2)//2](nn, *arg2)
print(nnn)