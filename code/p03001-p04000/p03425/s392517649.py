import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    def select(n,k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    n = I()
    dic = collections.defaultdict(int)
    for _ in range(n):
        s = S()
        if s[0] in {"M","A","R","C","H"}:
            dic[s[0]] += 1

    vlst = [i for i in dic.values() if i!=0]
    ans = 0
    lenth = len(vlst)

    for i in range(lenth):
        for j in range(i+1,lenth):
            for k in range(j+1,lenth):
                ans += select(vlst[i],1)*select(vlst[j],1)*select(vlst[k],1)
    print(ans)
main()            
