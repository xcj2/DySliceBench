import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    d = LI()
    m = I()
    t = LI()
    ddic = collections.Counter(d)
    tdic = collections.Counter(t)

    for i in tdic.keys():
        sub = max(0,tdic[i]-ddic.get(i,0))
        if sub > 0:
            print("NO")
            break
    else:
        print("YES")
main()