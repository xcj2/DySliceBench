import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    v = LI()
    acnt = collections.Counter(v[::2])
    bcnt = collections.Counter(v[1::2])
    acnt = list(acnt.items())
    bcnt = list(bcnt.items())
    acnt.sort(key=lambda x: x[1], reverse=True)
    bcnt.sort(key=lambda x: x[1], reverse=True)

    acnt.append((-1,0))
    bcnt.append((-1,0))

    ans = 0

    if acnt[0][0] != bcnt[0][0]:
        ans = n - acnt[0][1] - bcnt[0][1]
    else:
        ans = min(n-acnt[0][1]-bcnt[1][1], n-acnt[1][1]-bcnt[0][1])

    print(ans)

main()
