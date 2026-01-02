import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    t = S()
    s = list(s)
    t = list(t)
    slen = len(s)
    tlen = len(t)
    ans = float("inf")

    for i in range(tlen):
        char = t[i]
        for j in range(i,slen-(tlen-i-1)):
            aaa = s[j]
            if aaa==char:
                rng = s[j:j+tlen-i]
                ex = t[i:]
                cnt = 0
                for x,y in zip(rng,ex):
                    if x == y:
                        cnt += 1
                ans = min(ans, tlen-cnt)
    if ans == float("inf"):
        ans = tlen
    print(ans)

main()            
