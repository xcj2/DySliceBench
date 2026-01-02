from heapq import heappush, heappop
from operator import itemgetter
import sys
input = sys.stdin.readline
#参考
#https://atcoder.jp/contests/abc128/submissions/15199101
class PseudoSet():
    def __init__(self):
        self.s = []  # set
        self.e = []  # erase candidate

    def insert(self, x):
        heappush(self.s, x)

    def erase(self, x):
        heappush(self.e, x)

    def get_min(self):
        while self.e and self.e[0] == self.s[0]:
            _ = heappop(self.s)
            _ = heappop(self.e)
        return self.s[0] if len(self.s) > 0 else None

def main():
    n,q=map(int, input().split())
    event = []
    end = []
    for i in range(n):
        s,t,x=map(int, input().split())
        event.append([s-x,1,x])
        event.append([t-x,0,x])

    for i in range(q):
        d = int(input())
        event.append([d,2,i])
    event.sort(key = itemgetter(0,1))
    res = [-1]*q
    ps = PseudoSet()
    for time,type,x in event:
        if(type==1):
            ps.insert(x)
        elif(type==0):
            ps.erase(x)
        else:
            k = ps.get_min()
            if k is not None:
                res[x]=k
    print(*res,sep="\n")

if __name__ == '__main__':
    main()
