import sys,collections;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

abc = "abcdefghijklmnopqrstuvwxyz"
s = S()
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
if len(s) < 26:
    for a in abc:
        if not a in s:
            print(s+a)
            exit()
else:
    for i in range(len(s)-1):
        if s[-i-2] < s[-i-1]:
            ans = s[:-i-2]
            t = s[-i-2]
            for a in abc:
                if not a in ans and a > t:
                    print(ans+a)
                    exit()
